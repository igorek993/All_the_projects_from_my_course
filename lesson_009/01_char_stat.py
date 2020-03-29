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
    # TODO Создайте метод __init__ где укажите атрибуты используемые классом

    def open_file(self, filename):
        # opens a file and returns it ready to be read
        with open(filename, 'r', encoding='cp1251') as file:
            return file.read()

    def get_stat(self, stat_file):
        # collects the letters statistic and returns it
        stat = {}
        for line in stat_file:
            for letter in line:
                if letter.isalpha():
                    if letter in stat:
                        stat[letter] += 1
                    else:
                        stat[letter] = 1
        return stat

    def count_total(self, stat_file):
        # counts total amount of letters
        letters_total = 0
        for key, value in stat_file.items():
            letters_total += value
        return letters_total

    def print(self, stat_file, total_letters):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        for key, value in stat_file.items():
            print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(total_letters))


class BookStat(StatisticCount):
# TODO Усложнили структуру наследования - этот шаблонный метод нужно поместить в базовый класс
    def start(self, file):
        initial_file = self.open_file(file)
        stat_file = self.get_stat(initial_file)

        # TODO Тут должне быть вызов сортировки

        total_count = self.count_total(stat_file)
        self.print(stat_file, total_count)


class BookStatAlphabetic(StatisticCount):
    # TODO Аналогично, этот метод обязан быть в базовом классе хотя бы как абстрактный, но на практике часто
    #  и базовый класс "рабочий"
    def sort_out(self, start_file):
        # sorts out a start file in an alphabetic order
        sorted_file = sorted(start_file.items())
        return sorted_file

# TOdO Это почти полный дубликат из базового класса, приведите атрибут stat_file обоих классов к одному типу, чтобы не
#  множить из-за мелочи варианты реализации методов
    def print(self, stat_file, total_letters):
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        for key, value in stat_file:
            print(f'|{key:^9}|{value:^10}|')
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(total_letters))

    def start(self, file):
        initial_file = self.open_file(file)
        stat_file = self.get_stat(initial_file)
        sorted_start_file = self.sort_out(stat_file)
        total_count = self.count_total(stat_file)
        self.print(sorted_start_file, total_count)
    # TODO Постарайте использовать шаблонный метод базового класса


class BookStatAlphabeticReverse(BookStatAlphabetic):

    def sort_out(self, start_file):
        # sorts out a start file in an alphabetic order
        sorted_file = sorted(start_file.items(), reverse=True)
        return sorted_file


class BookStatFrequency(BookStatAlphabetic):

    def sort_out(self, start_file):
        # sorts out a start file in an alphabetic order
        sorted_file = sorted(start_file.items(), key=lambda x: x[1], reverse=True)
        return sorted_file


# stat_counter = BookStatFrequency()
stat_counter = BookStatAlphabetic()

stat_counter.start(FILE_NAME)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
