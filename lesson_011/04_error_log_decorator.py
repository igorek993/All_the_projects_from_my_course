# -*- coding: utf-8 -*-
from termcolor import colored


# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

# TODO Question!!! is it possible to make the log file colored? So (Function name,parameters, exception type)
#  would have green color?

def log_errors(func):
    def surrogate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            with open('function_errors.log', 'a') as log:
                log.write(f'\nFunction name: {str(func)}, parameters: {str(*args, **kwargs)}, '
                          f'exception type: {type(exception).__name__} exception message: {exception.args}')
                raise exception
    return surrogate


# Проверить работу на следующих функциях

@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not an email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age is not in 10 to 99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
