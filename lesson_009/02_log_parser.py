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

    def __init__(self, file_to_read, result):
        self.file_to_read = file_to_read
        self.result = result
        self.count = 0
        self.previous_time = []
        self.allow = True
        self.line_slice = slice(0, 17)  # TODO Сделайте присвоение значения атрибуту в отдельном методе, а в наследниках
        # переопределяйте этот метод - будет намного лаконичнее, чем через конструктор

    def get_data(self):
        with open(self.file_to_read, 'r') as file:
            return file.readlines()

    def give_result(self):
        with open(self.result, 'w') as result:
            for line in self.get_data():
                if self.previous_time:
                    if self.previous_time == line[self.line_slice] and line[29:32] == 'NOK':
                        self.count += 1
                    elif self.previous_time != line[self.line_slice]:
                        result.write(f'{self.previous_time}] {self.count} \n')
                        self.count = 0
                        self.allow = True
                        self.previous_time = []
                self.check_if_nok(line)

    def check_if_nok(self, line):
        if line[29:32] == 'NOK' and self.allow:
            self.count += 1
            self.previous_time = line[self.line_slice]
            self.allow = False


class ReadFileHours(ReadFile):

    def __init__(self, file_to_read, result):
        super().__init__(file_to_read, result)
        self.line_slice = slice(0, 14)


class ReadFileMonth(ReadFile):

    def __init__(self, file_to_read, result):
        super().__init__(file_to_read, result)
        self.line_slice = slice(0, 8)

    def give_result(self):
        with open(self.result, 'w') as result:
            for line in self.get_data():
                if self.previous_time:
                    if self.previous_time == line[self.line_slice] and line[29:32] == 'NOK':
                        self.count += 1
                    elif self.previous_time != line[self.line_slice]:
                        result.write(f'{self.previous_time}] {self.count} \n')
                        self.count = 0
                        self.allow = True
                        self.previous_time = []
                self.check_if_nok(line)
            result.write(f'{self.previous_time}] {self.count} \n')
            # TODO Алгоритм этого метод содержит ошибку - исправьте её и переопределять метод не понадобится


class ReadFileYear(ReadFileMonth):

    def __init__(self, file_to_read, result):
        super().__init__(file_to_read, result)
        self.line_slice = slice(0, 5)


a = ReadFile(FILE_TO_READ, RESULT)
a.give_result()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
