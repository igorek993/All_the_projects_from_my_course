from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from bot import Bot
from vk_api.bot_longpoll import VkBotMessageEvent


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

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=self.RAW_EVENT['object']['message']['text'],
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )
