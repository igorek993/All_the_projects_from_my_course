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


    def open_file_read(self, file_to_read):
        with open(file_to_read, 'r') as file:
            return file.readlines()

    def sort(self, previous_time, count, file_to_read):
        for line in file_to_read:
            if previous_time:
                if previous_time == line[slice(0, 17)] and line[29:32] == 'NOK':
                    count += 1
                elif previous_time != line[slice(0, 17)]:
                    return previous_time, line
            return previous_time, line

    def write_result(self, previous_time, count ,result_file):
        with open(result_file, 'w') as result:
            result.write(f'{previous_time}] {count} \n')
            count = 0
            allow = True
            previous_time = []

    def check_if_nok(self, line, count):
        if line[29:32] == 'NOK' and allow:
            count += 1
            previous_time = line[slice(0, 17)]
            allow = False

    # TODO Cоздайте четкие "однозадачные" шаги и перечислите их в шаблонном методе с именем "запустить"

    def start(self, read_file):
        file_to_read = self.open_file_read(read_file)
        count = 0
        previous_time = False
        self.sort(previous_time, count, file_to_read)








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
            for line in self.open_file():
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
