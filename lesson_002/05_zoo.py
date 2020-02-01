#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

zoo.extend(birds)  # Другой вариант: zoo += birds
print(zoo)

# уберите слона
#  и выведите список на консоль

del zoo[3]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion_cell_number = zoo.index('lion') + 1
lark_cell_number = zoo.index('lark') + 1
print('the lion is in the cell number: ', lion_cell_number, 'the lark is in the cell number: ', lark_cell_number)
