# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import pprint
from lesson_005.district.central_street.house1.room1 import folks as folks_1_h1_r1
from lesson_005.district.central_street.house1.room2 import folks as folks_2_h1_r2
from lesson_005.district.central_street.house2.room1 import folks as folks_3_h2_r1
from lesson_005.district.central_street.house2.room2 import folks as folks_4_h2_r2
from lesson_005.district.soviet_street.house1.room1 import folks as folks_5_h1_r1
from lesson_005.district.soviet_street.house1.room2 import folks as folks_6_h1_r2
from lesson_005.district.soviet_street.house2.room1 import folks as folks_7_h2_r1
from lesson_005.district.soviet_street.house2.room2 import folks as folks_8_h2_r2

people = folks_1_h1_r1 + folks_2_h1_r2 + folks_3_h2_r1 + folks_4_h2_r2 + folks_5_h1_r1 + \
         folks_6_h1_r2 + folks_7_h2_r1 + folks_8_h2_r2
print('На районе живут:', ', '.join(people))

# I understood you in a wrong way and started making up a filter an a small database for the all the people to
# extract the data afterwards. But apparently, I just had to change the names of the variables after as...
# that was funny...
# Не имена, а способ объединения списков мы изменили

# folks_data = {
#     'central_street': [
#         {'house number': 'house_1', 'rooms': [
#             {'room_number': 'room_1', 'folks': folks_1},
#             {'room_number': 'room_2', 'folks': folks_2}]},
#
#         {'house number': 'house_2', 'rooms': [
#             {'room_number': 'room_1', 'folks': folks_3},
#             {'room_number': 'room_2', 'folks': folks_4}]}
#     ],
#     'soviet_street': [
#         {'house number': 'house_1', 'rooms': [
#             {'room_number': 'room_1', 'folks': folks_5},
#             {'room_number': 'room_2', 'folks': folks_6}]},
#
#         {'house number': 'house_2', 'rooms': [
#             {'room_number': 'room_1', 'folks': folks_7},
#             {'room_number': 'room_2', 'folks': folks_8}]}
#     ]
#
# }
#
# for i, c in enumerate(people):
#     for d, f in enumerate(people):
#         if c == f:
#             if i == d:
#                 continue
#             elif i != d:
#                 print(c)

# зачет!
