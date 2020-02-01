#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'candy': [
        {'shop': 'coles', 'price': 0.2},
        {'shop': 'ig', 'price': 0.3},
        {'shop': 'aldi', 'price': 0.35},
        {'shop': 'woolworth', 'price': 0.4},
    ],
    'lollipop':[
        {'shop': 'coles', 'price': 0.1},
        {'shop': 'ig', 'price': 0.5},
        {'shop': 'aldi', 'price': 1.35},
        {'shop': 'woolworth', 'price': 4.4},
    ]
}

# Указать надо только по 2 магазина с минимальными ценами

