#!/usr/bin/env python3
# coding=utf8
import logging
import random

import handlers
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

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


class UserSate:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


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
        self.user_state = dict()  # user_id → UserState

    def run(self):
        """
        Start the bot
        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('error while processing the event')

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
        if user_id in self.user_state:
            text_to_send = self.continue_scenario(user_id, text=text)
        else:
            for intent in settings.INTENTS:
                log.debug(f"User gets {intent}")
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id)

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_state[user_id] = UserSate(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_state[user_id]
        step = settings.SCENARIOS[state.scenario_name]['steps'][state.step_name]
        steps = settings.SCENARIOS[state.scenario_name]['steps']

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                # swich to next step
                state.step_name = step['next_step']
            else:
                # scenario finished
                log.info(state.context)
                self.user_state.pop("Registered: {name} {email}".format(**state.context))
                # todo Уверены что такой ключ существует в self.user_state? Не так ли должно быть:
                # self.user_state.pop(user_id) ??
        else:
            # repeat current step
            text_to_send = step['failure_text'].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
