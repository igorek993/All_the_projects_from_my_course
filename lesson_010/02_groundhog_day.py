# -*- coding: utf-8 -*-

import random
from termcolor import cprint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __init__(self):
        self.message = 'Thought he was God today'

    def __str__(self):
        return self.message


class DrunkError(Exception):

    def __init__(self):
        self.message = 'Got too drunk'

    def __str__(self):
        return self.message


class CarCrashError(Exception):

    def __init__(self):
        self.message = 'Had a car crash'

    def __str__(self):
        return self.message


class GluttonyError(Exception):

    def __init__(self):
        self.message = 'Overate'

    def __str__(self):
        return self.message


class DepressionError(Exception):

    def __init__(self):
        self.message = 'Was in depression'

    def __str__(self):
        return self.message


class SuicideError(Exception):

    def __init__(self):
        self.message = 'Tried to commit suicide'

    def __str__(self):
        return self.message


exceptions_list = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]


def one_day():
    carma_upgrade = random.randint(1, 7)
    if random.randint(1, 13) == 1:
        raise exceptions_list[random.randint(0, 5)]
    return carma_upgrade


carma_level = 0
day = 0
while carma_level < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        carma_level += one_day()
        day += 1
        print(f'day {day}, carma level {carma_level}')
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exp:
        cprint(exp, color='yellow')
