#!/usr/bin/env python3
# coding=utf8

from chatbot.my_token import token
import vk_api
import vk_api.bot_longpoll
import random

group_id = 194838302


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('Notification')
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            self.api.messages.send(message=(event.object['message']['text']),
                                   random_id=random.randint(0, 2 ** 20),
                                   peer_id=event.object['message']['peer_id'])
        else:
            print('We are not sure how to process this yet', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
