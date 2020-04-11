# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

FILE_TO_READ = 'events.txt'


def log_reader(file_to_read):
    with open(file_to_read, 'r') as file:
        count = 0
        previous_time = []
        allow = True
        for line in file:
            current_slice = line[0:17]
            if previous_time:
                if previous_time == current_slice and 'NOK' in line:
                    count += 1
                elif previous_time != current_slice:
                    yield previous_time, count
                    count = 0
                    allow = True
                    previous_time = []
            if 'NOK' in line and allow:
                count += 1
                previous_time = current_slice
                allow = False


grouped_events = log_reader(FILE_TO_READ)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
