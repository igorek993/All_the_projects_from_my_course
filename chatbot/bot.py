#!/usr/bin/env python3
# coding=utf8
import logging
import random

import handlers
import requests
import vk_api
from pony.orm import db_session
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from chatbot.models import UserState, Registration

try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token!')

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log')
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s", '%d-%m-%Y %H:%M:'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot for vk.com
    Use python 3.7
    """

    def __init__(self, group_id, token):
        """
        :param group_id: group id from vk group
        :param token: secret token
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """
        Start the bot
        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('error while processing the event')

    @db_session
    def on_event(self, event):
        """
        sends a text message back to the user
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('We are not sure how to process this yet %s', event.type)
            return

        user_id = event.object['message']['peer_id']
        text = event.object['message']['text']
        state = UserState.get(user_id=str(user_id))

        if state is not None:
            self.continue_scenario(text, state, user_id)
        else:
            for intent in settings.INTENTS:
                log.debug(f"User gets {intent}")
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        self.send_text(intent['answer'], user_id)
                    else:
                        self.start_scenario(user_id, intent['scenario'], text)
                    break
            else:
                self.send_text(settings.DEFAULT_ANSWER, user_id)

    def send_text(self, text_to_send, user_id):
        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id)

    def send_image(self, image, user_id):
        upload_url = self.api.photos.getMessagesUploadServer()["upload_url"]
        upload_data = requests.post(url=upload_url, files={'photo': ('image.png', image, 'image/png')}).json()
        image_data = self.api.photos.saveMessagesPhoto(**upload_data)

        owner_id = image_data[0]["owner_id"]
        media_id = image_data[0]["id"]
        attachment = f'photo{owner_id}_{media_id}'

        self.api.messages.send(message=attachment,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id)

    def send_step(self, step, user_id, text, context):
        if "text" in step:
            self.send_text(step['text'].format(**context), user_id)
        if "image" in step:
            handler = getattr(handlers, step['image'])
            image = handler(text, context)
            self.send_image(image, user_id)

    def start_scenario(self, user_id, scenario_name, text):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        self.send_step(step, user_id, text, context={})
        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step, context={})

    def continue_scenario(self, text, state, user_id):
        step = settings.SCENARIOS[state.scenario_name]['steps'][state.step_name]
        steps = settings.SCENARIOS[state.scenario_name]['steps']

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step['next_step']]
            self.send_step(next_step, user_id, text, state.context)
            if next_step['next_step']:
                # swich to next step
                state.step_name = step['next_step']
            else:
                # scenario finished
                Registration(name=state.context["name"], email=state.context["email"])
                log.info(state.context)
                state.delete()
        else:
            # repeat current step
            text_to_send = step['failure_text'].format(**state.context)
            self.send_text(text_to_send, user_id)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
