# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
BRUCE_WILLIS = 42


def wired_function():
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")


# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

try:
    wired_function()
except ValueError:
    print('невозможно преобразовать к числу')
except IndexError:
    print('выход за границы списка')
except BaseException as exp:
    print(f'что то пошло не так{exp}')

# зачет!
