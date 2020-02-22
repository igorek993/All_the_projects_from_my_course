import random

numbers = []
count = 1
let_it_go = True


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


user_number = []
user_input = 0


def number_ask_filter_1():
    global user_input
    while True:
        a = 0
        user_input = input()
        if len(user_input) > 4:
            print('too long')
            number_ask_filter_1()
        elif len(user_input) < 4:
            print('too short')
            number_ask_filter_1()
        elif user_input[0] == '0':
            print('the first digit can not be 0')
            number_ask_filter_1()
        elif user_input.isnumeric():
            break
        else:
            print('only numbers')
            number_ask_filter_1()
        break


def number_ask_filter_2():
    global user_input
    global user_number
    global let_it_go
    let_it_go = True
    user_number = []
    for i in user_input:
        user_number.append(int(i))
        print(user_number)
    for b in user_number:
        count_1 = 0
        for c in user_number:
            if b == c:
                count_1 += 1
            if count_1 == 2:
                print('There can not be two similar digits')
                let_it_go = False
                return let_it_go


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
        print(bulls_and_cows)
    count = count + 1
    user_number = []


def game_over():
    return bulls_and_cows['bulls'] == 4
