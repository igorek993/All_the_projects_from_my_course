#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Стол
table_code = store[goods['Стол']]
# TODO table_item_1(2) дважды используются в расчётах, а читаются они лучше чем индексы

# I am sorry, I did not quite understand your last comment. Would you be able to give me an example of what I should do
# and what you mean when you use the word ´index´?
# Thank you!

table_quantity_1 = table_code[0]['quantity']
# TODO here you use table_code variable with an index 0 (see below too)
table_quantity_2 = table_code[1]['quantity']
tables_quantity_total = table_quantity_1 + table_quantity_2
table_price_1 = table_code[0]['price']
# TODO and here the same table_code[0], my suggestion is: create new variable table_item_1 = table_code[0] and
#  use it instead of indexing the table_code
table_price_2 = table_code[1]['price']
table_cost_total = (table_quantity_1 * table_price_1) + (table_quantity_2 * table_price_2)

print('There are', tables_quantity_total, 'tables in the warehouse,', 'their total value is', table_cost_total, 'rub')

# Диван
couch_code = store[goods['Диван']]
couch_quantity_total = couch_code[0]['quantity'] + couch_code[1]['quantity']
couch_quantity_1 = couch_code[0]['quantity']
couch_quantity_2 = couch_code[1]['quantity']
couch_price_1 = couch_code[0]['price']
couch_price_2 = couch_code[1]['price']
couch_cost_total = (couch_quantity_1 * couch_price_1) + (couch_quantity_2 * couch_price_2)

print('There are', couch_quantity_total, 'couches in the warehouse,', 'their total value is', couch_cost_total, 'rub')

# Стул
chair_code = store[goods['Стул']]
chair_quantity_1 = chair_code[0]['quantity']
chair_quantity_2 = chair_code[1]['quantity']
chair_quantity_3 = chair_code[2]['quantity']
chair_quantity_general = chair_quantity_1 + chair_quantity_2 + chair_quantity_3
chair_price_1 = chair_code[0]['price']
chair_price_2 = chair_code[1]['price']
chair_price_3 = chair_code[2]['price']
chair_cost_total = (chair_quantity_1 * chair_price_1) + (chair_quantity_2 * chair_price_2) + (
        chair_quantity_3 * chair_price_3)

print('There are', chair_quantity_general, 'chairs in the warehouse,', 'their total value is', chair_cost_total, 'rub')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
