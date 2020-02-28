# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'I am - {}, fullness {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} had some food'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} there is no food'.format(self.name), color='red')

    def work(self):
        cprint('{} worked today'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} was watching MTV all day long'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} bought some groceries'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} ran out of money!'.format(self.name), color='red')

    def move_to_a_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} moved to a house'.format(self.name), color='cyan')

    def take_cat_home(self, cat):
        cat.house = self.house
        print('I like this kitty!')

    def buy_cat_food(self):
        if self.house.money > 50:
            self.house.food_bowl_fullness += 50
            self.house.money -= 50
            print('{} bought some cat food'.format(self.name))
        else:
            print('{} wanted to buy cat food but there was no money'.format(self.name))
            self.work()

    def clean_the_house(self):
        self.house.cleanliness += 100
        self.fullness -= 20
        print('{} cleaned the house'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            cprint('{} passed away...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money < 100:
            self.work()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.food_bowl_fullness <= 60:
            self.buy_cat_food()
        elif self.house.cleanliness <= 5:
            self.clean_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_bowl_fullness = 0
        self.cleanliness = 100

    def __str__(self):
        return 'There is {} food left in the house, money {} left, cleanliness is {}, cat food is {} '.format(
            self.food, self.money, self.cleanliness, self.food_bowl_fullness)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'I am {} and my fullness is {}'.format(self.name, self.fullness)

    def sleep(self):
        self.fullness -= 10
        print('{} slept all day long'.format(self.name))

    def eat(self):
        if self.house.food_bowl_fullness >= 10:
            self.fullness += 20
            self.house.food_bowl_fullness -= 10
            print('{} has eaten'.format(self.name))
        else:
            self.fullness -= 10
            print('{} looked for food but found nothing...'.format(self.name))

    def scratch_the_wallpapers(self):
        self.fullness -= 10
        self.house.cleanliness -= 5
        print('{} scratched the wallpapers'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} passed away...'.format(self.name))
            return
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.scratch_the_wallpapers()
        elif dice == 2:
            self.sleep()


my_sweet_home = House()
cats = [
    Cat(name='Barsik'),
    Cat(name='Kusia'),
    Cat(name='Mursik')
]
sam = Man(name='Sam')
sam.move_to_a_house(house=my_sweet_home)
for cat in cats:
    sam.take_cat_home(cat=cat)

for day in range(1, 366):
    print('================ day {} =================='.format(day))
    for cat in cats:
        cat.act()
    sam.act()
    print('--- in the end of the day ---')
    print(sam)
    print(my_sweet_home)
    for cat in cats:
        print(cat)

# hahahaha it's a funny comment... The thing is that I speak English/Spanish/Russian every day mixing them up together
# every hour depending who I should talk to. That is why for me it's like a common thing to have a
# mixture of these three languages everywhere. If you could only take a look at my notes from my Master's degree, it's
# a mess of these three languages, no one can read them :D. I am sorry for that, I did not
# think about it for some reason, I'll change everything to English.
# Интересная у вас работа, видимо! Сам учил английский всю жизнь и абсолютно его не знал кроме некоторого словарного
# запаса... и только когда припекло выучился читать более-менее, статьи по технике и художку читаю.

# зачет!

