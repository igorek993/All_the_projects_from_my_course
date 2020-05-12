#!/usr/bin/env python3
# coding=utf8
import logging

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

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

    def on_event(self, event):
        """
        sends a text message back to the user
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('sending a message')
            self.api.messages.send(message=(event.object['message']['text']),
                                   random_id=random.randint(0, 2 ** 20),
                                   peer_id=event.object['message']['peer_id'])
        else:
            log.info('We are not sure how to process this yet %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
