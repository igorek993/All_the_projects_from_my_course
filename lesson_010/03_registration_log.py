# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
REG_LOG = 'registrations.txt'
GOOD_DATA = 'registrations_good.txt'
BAD_DATA = 'registrations_bad.txt'


class NotNameError(Exception):

    def __init__(self):
        self.message = 'unexpected sign in the name (only letters)'

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self):
        self.message = 'email should have . and @ in it'

    def __str__(self):
        return self.message


class Filter:

    def __init__(self, file_to_scan):
        self.file_to_scan = file_to_scan
        self.registrations_good = []
        self.registrations_bad = []

    def file_scan(self):
        line_number = 0
        with open(self.file_to_scan, 'r', encoding='utf8') as log:
            for line in log:
                line_number += 1
                try:
                    name, email, age = line.split(' ')
                    if self.name_check(name) and self.email_check(email) and self.age_check(int(age)):
                        self.registrations_good.append(line)
                except ValueError as ve:
                    self.registrations_bad.append(f'{ve} in line {line_number}, {line}')
                except NotEmailError as ne:
                    self.registrations_bad.append(f'{ne} in line {line_number}, {line}')
                except NotNameError as nn:
                    self.registrations_bad.append(f'{nn} in line {line_number}, {line}')

    def age_check(self, age):
        if 99 >= age >= 10:
            return True
        else:
            raise ValueError('age is not an int in a range 10 to 99')

    def email_check(self, email):
        if '.' and '@' in email:
            return True
        else:
            raise NotEmailError

    def name_check(self, name):
        if name.isalpha():
            return True
        else:
            raise NotNameError

    def write_results(self):
        with open(GOOD_DATA, 'w+') as good_log:
            for line in self.registrations_good:
                good_log.write(line)
        with open(BAD_DATA, 'w+') as bad_log:
            for line in self.registrations_bad:
                bad_log.write(line)

    def run(self):
        self.file_scan()
        self.write_results()


log_reader = Filter(REG_LOG)
log_reader.run()
