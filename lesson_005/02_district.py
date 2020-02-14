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

suburb_list = [folks_1, folks_2, folks_3, folks_4, folks_5, folks_6, folks_7, folks_8]
a = ','

print('На районе живут', a.join(folks_1) + ',', a.join(folks_2) + ',', a.join(folks_3), a.join(folks_4) + ',',
      a.join(folks_5) + ',', a.join(folks_6) + ',', a.join(folks_7) + ',', a.join(folks_8))
