import random

numbers = []
count = 1


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


def number_check(user_number_raw):
    global count
    global bulls_and_cows
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    user_number = []
    for i in user_number_raw:
        user_number.append(int(i))
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


def game_over():
    return bulls_and_cows['bulls'] == 4
