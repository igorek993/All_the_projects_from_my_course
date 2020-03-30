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
        self.stat_file = None
        self.letters_total = 0
        self.sorted_file = None
        self.file_to_read = None
        self.stat_file_sorted = None

    def open_file(self):
        # opens a file and returns it ready to be read
        with open(self.filename, 'r', encoding='cp1251') as file:
            self.file_to_read = file.read()

    def get_stat(self):
        # collects the letters statistic and returns it
        stat = {}
        for line in self.file_to_read:
            for letter in line:
                if letter.isalpha():
                    if letter in stat:
                        stat[letter] += 1
                    else:
                        stat[letter] = 1
        self.stat_file = stat

    def count_total(self):
        # counts total amount of letters
        letters_total = 0
        for key, value in self.stat_file.items():
            letters_total += value
        self.letters_total = letters_total

    def sort_out(self, reverse):
        # sorts out a start file in an alphabetic order
        self.stat_file_sorted = sorted(self.stat_file.items(), reverse=reverse)

    def print(self):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        if self.stat_file_sorted:
            for key, value in self.stat_file_sorted:
                print(f'|{key:^9}|{value:^10}|')
        else:
            for key, value in self.stat_file.items():
                print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(self.letters_total))

    def run(self):
        self.open_file()
        self.get_stat()
        self.count_total()
        self.print()


class BookStatAlphabetic(StatisticCount):

    def run(self):
        self.open_file()
        self.get_stat()
        self.count_total()
        self.sort_out(reverse=False)
        self.print()


class BookStatAlphabeticReverse(BookStatAlphabetic):

    def run(self):
        self.open_file()
        self.get_stat()
        self.count_total()
        self.sort_out(reverse=True)
        self.print()


class BookStatFrequency(BookStatAlphabetic):

    def sort_out(self, reverse):
        self.stat_file_sorted = sorted(self.stat_file.items(), key=lambda x: x[1], reverse=True)


# stat_counter = BookStatFrequency()
stat_counter = BookStatFrequency(FILE_NAME)
stat_counter.run()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
