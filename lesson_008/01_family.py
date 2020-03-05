# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirtiness = 0

    def __str__(self):
        return 'There are {} dollars, {} food left in the house. The tidiness level is {}'.format(self.money, self.food,
                                                                                                  self.dirtiness)

    def act(self):
        self.dirtiness += 5


class People:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return 'I am {}, my fullness is {}, my happiness {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.fullness += 30


class Husband:

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def work(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.house.money += 150
            return '{} worked for the whole day'.format(self.name)
        else:
            return 'not enough food to be able to get to work'

    def gaming(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.happiness += 20
            return '{} played WoT for the whole day'.format(self.name)
        else:
            '{} cant play while hungry'.format(self.name)


class Wife:

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def shopping(self):
        if self.house.money >= 60:
            self.house.food -= 10
            self.house.money -= 60
            self.house.food += 60
            return '{} bought some food'.format(self.name)
        else:
            return 'not enough money to buy food'

    def buy_fur_coat(self):
        if self.house.food >= 10 and self.house.money >= 350:
            self.house.food -= 10
            self.house.money -= 350
            self.happiness += 60
            return '{} bought a new coat'.format(self.name)

    def clean_house(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.house.dirtiness -= 30
            return '{} cleaned the house'.format(self.name)


home = House()
sergey = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.act()
    sergey.act()
    masha.act()
    cprint(sergey, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
