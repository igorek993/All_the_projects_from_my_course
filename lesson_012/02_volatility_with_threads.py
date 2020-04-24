# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
import os
import time
from threading import Thread

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


class StockAnalyst(Thread):

    def __init__(self, file_dir, file, volatility_dict):
        super().__init__()
        self.volatility_dict = volatility_dict
        self.file = file
        self.file_dir = file_dir
        self.current_stock_info_list = list()
        self.current_secid = None
        self.current_min_price = 0
        self.current_max_price = 0
        self.current_average_price = 0
        self.current_volatility = 0

    def run(self):
        global done
        self.get_stock_info(self.file)
        self.find_min_max_price()
        self.calculate_volatility_average_price()
        self.volatility_dict.update({self.current_secid: round(self.current_volatility, 2)})

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

stock_analysts = [StockAnalyst(FILES_DIRECTORY, file, volatility_dict=volatility_dict) for file in
                  os.listdir(FILES_DIRECTORY)]


@time_track
def analyze_stocks():
    for analyst in stock_analysts:
        analyst.start()
    for analyst in stock_analysts:
        analyst.join()
    print_report(volatility_dict)


analyze_stocks()
