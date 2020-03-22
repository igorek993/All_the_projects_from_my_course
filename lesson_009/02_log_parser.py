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

# the length of a line is 32 , up to minutes is 17, the last letters [29:32], minute digit is [16]

class ReadFile:

    def give_a_result(self, file_to_read, result):
        with open(file_to_read, 'r') as file:
            with open(result, 'w') as result:
                count = 0
                previous_time = []
                allow = True
                for line in file:
                    if previous_time:
                        if previous_time == line[0:17] and line[29:32] == 'NOK':
                            count += 1
                        elif previous_time != line[0:17]:
                            result.write(f'{previous_time}] {count} \n')
                            count = 0
                            allow = True
                            previous_time = []
                    if line[29:32] == 'NOK' and allow:
                        count += 1
                        previous_time = line[0:17]
                        allow = False


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


file_to_read = 'events.txt'
result = 'result.txt'

a = ReadFile()

a.give_a_result(file_to_read=file_to_read, result=result)
