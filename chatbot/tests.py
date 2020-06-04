#!/usr/bin/env python3
# coding=utf8

from copy import deepcopy
from pprint import pprint
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from bot import Bot
from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEvent

from chatbot import settings


class Test1(TestCase):
    RAW_EVENT = {'type': 'message_new', 'object': {'message': {'date': 1589458882, 'from_id': 595122526, 'id': 127,
                                                               'out': 0, 'peer_id': 595122526, 'text': 'm,ss',
                                                               'conversation_message_id': 120, 'fwd_messages': [],
                                                               'important': False, 'random_id': 0, 'attachments': [],
                                                               'is_hidden': False},
                                                   'client_info': {
                                                       'button_actions': ['text', 'vkpay', 'open_app', 'location',
                                                                          'open_link'],
                                                       'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}},
                 'group_id': 194838302, 'event_id':
                     '79e76d0f4e17e827dc0f67344f67d6f9c60455b0'}

    def test_ok(self):
        count = 5
        events = [{}] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.asserd_called()
                bot.on_event.asserd_any_call({})
                assert bot.on_event.call_count == count

    INPUTS = [
        "Привет",
        "А когда?",
        "Где будет конференция",
        "Зарегистритруй меня",
        "Вениамин",
        "мой адрес email@email",
        "email@email.ru",
    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]["answer"],
        settings.INTENTS[1]["answer"],
        settings.SCENARIOS["Registration"]["steps"]["step1"]["text"],
        settings.SCENARIOS["Registration"]["steps"]["step2"]["text"],
        settings.SCENARIOS["Registration"]["steps"]["step2"]["failure_text"],
        settings.SCENARIOS["Registration"]["steps"]["step3"]["text"].format(name="Вениамин", email="email@email.ru")
    ]

    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['text'] = input_text
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot("", "")
            bot.api = api_mock
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs["message"])
        assert real_outputs == self.EXPECTED_OUTPUTS
