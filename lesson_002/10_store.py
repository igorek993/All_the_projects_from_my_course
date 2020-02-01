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

#Стол
tables_quantity_general =store[goods['Стол']][0]['quantity']+ store[goods['Стол']][1]['quantity']
tables_t_1_q = store[goods['Стол']][0]['quantity']
tables_t_2_q = store[goods['Стол']][1]['quantity']
tables_t_1_p = store[goods['Стол']][0]['price']
tables_t_2_p = store[goods['Стол']][1]['price']

tables_sum = (tables_t_1_q * tables_t_1_p) + (tables_t_2_q * tables_t_2_p)

print('There are', tables_quantity_general, 'tables in the warehouse,', 'their total value is', tables_sum, 'rub')
# TODO К точности расчётов вопросов нет. Но такой код сложно читать и изменять. Названия переменны следует делать
#  полными словами, сокращения лучше не использовать или только в редких случаях. Введите переменные table_code,
#  table_item_1, table_quantity_1, table_price_1, table_item_2, table_quantity_2, table_price_2, table_cost_1,
#  table_cost_2, table_quantity_total, table_cost_total. Такой код называется "самокомменирующим кодом", имена
#  переменных комментируют его не хуже отдельных комментариев.
#  Для остальной мебели надо сделать также.

#Диван
couch_quantity_general = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
couch_t_1_q=store[goods['Диван']][0]['quantity']
couch_t_2_q=store[goods['Диван']][1]['quantity']
couch_t_1_p=store[goods['Диван']][0]['price']
couch_t_2_p=store[goods['Диван']][1]['price']
couch_sum = (couch_t_1_q * couch_t_1_p) + (couch_t_2_q*couch_t_2_p)

print('There are', couch_quantity_general, 'couches in the warehouse,', 'their total value is', couch_sum, 'rub')

#Стул

chair_quantity_general = store[goods['Стул']][0]['quantity']+store[goods['Стул']][1]['quantity']+store[goods['Стул']][2]['quantity']
chair_t_1_q=store[goods['Стул']][0]['quantity']
chair_t_2_q=store[goods['Стул']][1]['quantity']
chair_t_3_q=store[goods['Стул']][2]['quantity']
chair_t_1_p=store[goods['Стул']][0]['price']
chair_t_2_p=store[goods['Стул']][1]['price']
chair_t_3_p=store[goods['Стул']][2]['price']

chair_sum= (chair_t_1_q*chair_t_1_p)+(chair_t_2_q*chair_t_2_p)+(chair_t_3_q*chair_t_3_p)
print('There are', chair_quantity_general, 'chairs in the warehouse,', 'their total value is', chair_sum, 'rub')

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






