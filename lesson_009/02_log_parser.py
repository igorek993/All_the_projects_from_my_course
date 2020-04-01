# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# the length of a line is 32, up to minutes is 17, up to hours is  the last letters [29:32], minute digit is [16]

FILE_TO_READ = 'events.txt'
RESULT = 'result.txt'


class ReadFile:

    def __init__(self):
        self.count = 0
        self.allow = True
        self.previous_time = []
        self.previous_time_data = []
        self.count_data = []
        self.slice = slice(0, 0)

    def slice_size(self):
        self.slice = slice(0, 17)

    def open_file_read(self, file_to_read):
        with open(file_to_read, 'r') as file:
            return file.readlines()

    def sort(self, file_to_read):
        for line in file_to_read:
            if self.previous_time:
                if 'NOK' in line and self.previous_time == line[self.slice]:
                    self.count += 1
                elif self.previous_time != line[self.slice]:
                    self.previous_time_data.append(self.previous_time)
                    self.count_data.append(self.count)
                    self.count = 0
                    self.allow = True
                    self.previous_time = []
            self.check_if_nok(line)

    def write_result(self, result_file):
        if self.count:
            self.previous_time_data.append(self.previous_time)
            self.count_data.append(self.count)
        with open(result_file, 'w+') as result:
            for i in range(len(self.previous_time_data)):
                result.write(f'{self.previous_time_data[i]}] {self.count_data[i]} \n')

    def check_if_nok(self, line):
        if 'NOK' in line and self.allow:
            self.count += 1
            self.previous_time = line[self.slice]
            self.allow = False

    def run(self, read_file, result_file):
        self.slice_size()
        file_to_read = self.open_file_read(read_file)
        self.sort(file_to_read)
        self.write_result(result_file)


class ReadFileHours(ReadFile):

    def slice_size(self):
        self.slice = slice(0, 14)


class ReadFileMonth(ReadFile):

    def slice_size(self):
        self.slice = slice(0, 8)


class ReadFileYear(ReadFileMonth):

    def slice_size(self):
        self.slice = slice(0, 5)


a = ReadFileMonth()
a.run(FILE_TO_READ, RESULT)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
