# -*- coding: utf-8 -*-

# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас

import os
import time

FILES_DIRECTORY = os.path.normpath('C:\\Users\igorek\PycharmProjects\python_base\lesson_012\\trades')


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


def print_report(volatility_dict):
    zero_volatility = list()
    sorted_volatility_dict = sorted(volatility_dict.items(), key=lambda x: x[1], reverse=True)
    for stock in reversed(sorted_volatility_dict):
        if stock[1] == 0.0:
            zero_volatility.append(stock[0])
            sorted_volatility_dict.remove(stock)
        zero_volatility.sort()
    print(f"    Maximum volatility:\n"
          f"{sorted_volatility_dict[0][0]:>11} - {sorted_volatility_dict[0][1]:}%\n"
          f"{sorted_volatility_dict[1][0]:>11} - {sorted_volatility_dict[1][1]:}%\n"
          f"{sorted_volatility_dict[2][0]:>11} - {sorted_volatility_dict[2][1]:}%\n"
          f"    Minimum volatility:\n"
          f"{sorted_volatility_dict[-1][0]:>11} - {sorted_volatility_dict[-1][1]:}%\n"
          f"{sorted_volatility_dict[-2][0]:>11} - {sorted_volatility_dict[-2][1]:}%\n"
          f"{sorted_volatility_dict[-3][0]:>11} - {sorted_volatility_dict[-3][1]:}%\n"
          f"     Zero volatility:\n"
          f"       {','.join(zero_volatility):}")


class StockAnalyst:

    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.current_stock_info_list = list()
        self.current_secid = None
        self.current_min_price = 0
        self.current_max_price = 0
        self.current_average_price = 0
        self.current_volatility = 0

    def run(self, file):
        self.get_stock_info(file)
        self.find_min_max_price()
        self.calculate_volatility_average_price()
        return {self.current_secid: round(self.current_volatility, 2)}

    def get_stock_info(self, file):
        with open(os.path.join(self.file_dir, file), 'r') as stock_xl:
            self.current_stock_info_list = stock_xl.read().splitlines()[1:]

    def calculate_volatility_average_price(self):
        self.current_average_price = (self.current_max_price + self.current_min_price) / 2
        self.current_volatility = ((self.current_max_price - self.current_min_price) / self.current_average_price) * 100

    def find_min_max_price(self):
        price_list = []
        for line in self.current_stock_info_list:
            self.current_secid, tradetime, price, quantity = line.split(',')
            price_list.append(float(price))
        price_list.sort()
        self.current_min_price = price_list[0]
        self.current_max_price = price_list[-1]


volatility_dict = dict()

test = StockAnalyst(FILES_DIRECTORY)


@time_track
def analyze_stocks():
    for file in os.listdir(FILES_DIRECTORY):
        volatility_dict.update(test.run(file))
    print_report(volatility_dict)


analyze_stocks()

# зачет!
