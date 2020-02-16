# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import pprint
from lesson_005.district.central_street.house1.room1 import folks as folks_1
from lesson_005.district.central_street.house1.room2 import folks as folks_2
from lesson_005.district.central_street.house2.room1 import folks as folks_3
from lesson_005.district.central_street.house2.room2 import folks as folks_4
from lesson_005.district.soviet_street.house1.room1 import folks as folks_5
from lesson_005.district.soviet_street.house1.room2 import folks as folks_6
from lesson_005.district.soviet_street.house2.room1 import folks as folks_7
from lesson_005.district.soviet_street.house2.room2 import folks as folks_8

people = [folks_1, folks_2, folks_3, folks_4, folks_5, folks_6, folks_7, folks_8]
suburb_list = []
for person in people:
    suburb_list.extend(person)
a = ','
# TODO Всё проще, намного проще! Просто сложите эти списки с помощью оператора сложения "+"
print('На районе живут:', ', '.join(suburb_list))  # TODO разделитель обычно пишут прямо с join как показал
# TOdO Кстати, сразу не обратил внимание - Вадим настаивает, чтобы у в синонимах содержалась кратко информация об улице,
#  доме и комнате. И это, конечно, удобнее!
