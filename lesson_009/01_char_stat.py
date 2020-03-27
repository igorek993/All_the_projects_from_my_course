# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import zipfile as zp
from pprint import pprint

FILE_NAME = 'voyna-i-mir.txt'


class StatisticCount:

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        # open the file and return it ready to be read
        with open(self.filename, 'r', encoding='cp1251') as file:
            return file.read()

    def get_stat(self):
        # collect the letters statistic
        stat = {}
        for line in self.get_data():
            for letter in line:
                if letter.isalpha():
                    if letter in stat:
                        stat[letter] += 1
                    else:
                        stat[letter] = 1
        return stat

    def count_total(self):
        # counts total amount of letters
        letters_total = 0
        for key, value in self.get_stat().items():
            letters_total += value
        return letters_total

    def print(self):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        for key, value in self.get_stat().items():
            print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(self.count_total()))
    # TODO Ещё раз: каждый метод должен выполнять что-то одно: один читает файл, другой собирает статистику,
    #  третий сортирует, четвертый печатает. Отдельно стоит метод "шаблонный", он определяет последовательность
    #  выполнения задачи: вызывает последовательно все эти "шаги". А сейчас все методы взаимосвязаны, все друг друга
    #  вызывают, метод печати ещё иногда (!) занимается сортировкой (!), что трудно для понимания, а паттерны придумали
    #  как раз для упрощения сложных программ.


class BookStat(StatisticCount):

    def __init__(self, filename):  # TODO Не требуется переопределять какой-либо метод базового класса, раз не
                                   #  добавляется новой/изменяется функциональности
        super().__init__(filename)

    def print_stat(self):
        self.count_total()
        self.print()


class BookStatAlphabetic(StatisticCount):

    def __init__(self, filename):  # TODO убираем
        super().__init__(filename)

    def print(self):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        for key, value in sorted(self.get_stat().items()):
            print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(self.count_total()))

    def print_stat(self):
        self.count_total()
        self.print()


class BookStatAlphabeticReverse(StatisticCount):

    def __init__(self, filename):  # TODO убираем
        super().__init__(filename)

    def print(self):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        for key, value in sorted(self.get_stat().items(), reverse=True):
            print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(self.count_total()))

    def print_stat(self):
        self.count_total()
        self.print()


class BookStatFrequency(StatisticCount):

    def __init__(self, filename):    # TODO убираем
        super().__init__(filename)

    def print(self):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')

        stat = sorted(self.get_stat().items(), key=lambda x: x[1], reverse=True)  # todo I do not completely understand
        # todo how it works, but it does...
        for key, value in stat:
            print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(self.count_total()))

    def print_stat(self):
        self.count_total()
        self.print()


stat_counter = BookStatFrequency(FILE_NAME)

stat_counter.print_stat()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
