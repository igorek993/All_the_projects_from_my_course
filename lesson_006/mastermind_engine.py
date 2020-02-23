import random

numbers = []


def make_up_a_number():
    global numbers
    numbers_to_choose = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = []
    numbers.append(random.choice(numbers_to_choose[1:10]))
    numbers_to_choose.remove(numbers[0])
    taken_number = 1
    for i in range(3):
        numbers.append(random.choice(numbers_to_choose))
        numbers_to_choose.remove(numbers[taken_number])
        taken_number = taken_number + 1
    print(numbers)


user_number = []


def user_input_check(user_input):  # TODO Функция проверки ввода пользователя просто идеальна - охватывает все варианты
                                   #  ошибок и сообщаяет о них. Единственное, её надо перенести в основной модуль игры.
                                   #  Как вы помните, текущий модуль не должен работать с консолью - это требование
                                   #  задания, цитата:
               # При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
               # Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
               # разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
               # Движок игры реализует только саму функциональность игры.
    if len(user_input) > 4:
        print('too long')
        return False
    elif len(user_input) < 4:
        print('too short')
        return False
    elif user_input[0] == '0':
        print('the first digit can not be 0')
        return False
    else:
        pass
    if user_input.isnumeric():
        pass
    else:
        print('only numbers')
        return False


def user_input_check_2(user_input):  # TODo На это загадочное название прошлый раз не указал и видимо вы решили, что
                                     #  оно достаточно очевидно? Это очевидно вам, в течении недели после сдачи. Может
                                     #  быть даже через месяц, но позже вы сами будете гадать - и что это такое?
                                     #  Кроме того - принт надо перенести в основной модуль
    global user_number
    user_number = []
    for i in user_input:
        user_number.append(int(i))
    for b in user_number:
        count_1 = 0
        for c in user_number:
            if b == c:
                count_1 += 1
            if count_1 == 2:
                print('There can not be two similar digits')
                return False


def number_check():
    global count
    global bulls_and_cows
    global user_number
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    for position, number in enumerate(user_number):
        for position_1, number_1 in enumerate(numbers):
            if number == number_1:
                if position == position_1:
                    bulls_and_cows['bulls'] += 1
                else:
                    bulls_and_cows['cows'] += 1
    if bulls_and_cows['bulls'] == 4:
        game_over()
    else:
        return print(bulls_and_cows)  # TODO Такую удивительную конструкцию вижу второй раз в жизни :) Это надо
                                      #  обязательно прояснить до конца - с одной строны вроде бы всё очевидно, а другой
                                      #  видимо что-то упустили из теории ранее и надо понять что именно.
                                      #  Подумайте над тем что происходит в return print(..).
                                      #  Какое значение возвращает print?


def game_over():
    return bulls_and_cows['bulls'] == 4
