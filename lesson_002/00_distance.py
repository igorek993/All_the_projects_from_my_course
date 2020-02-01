# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distance = {}

moscow = cities['Moscow']
london = cities ['London']
paris = cities['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5

distance['Moscow'] = {}
distance ['Moscow']['London'] = moscow_london
distance ['Moscow']['Paris'] = moscow_paris

london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
london_moscow = ((london[0] - moscow[0]) ** 2 + (london[1] - moscow[1]) ** 2) ** .5
# TODO Излишнее вычисление, расстояния Москва-Лондон и Лондон-Москва равны
distance['London'] = {}
distance ['London']['Moscow'] = london_moscow
distance ['London']['Paris'] = london_paris

distance ['Paris'] = {}
distance ['Paris'] ['London'] = london_paris
distance ['Paris'] ['Moscow'] = moscow_paris

pprint(distance)

print(distance ['Paris']['Moscow'])


