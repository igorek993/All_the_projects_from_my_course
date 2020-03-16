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
        self.food_eaten = 0
        self.cat_food = 30
        self.cat = None
        self.residents = []
        self.cat_food_eaten = 0

    def __str__(self):
        return (
            'There are {} dollars, {} food, {} cat food left in the house. '
            'The dirtiness level is {}'.format(self.money, self.food, self.cat_food, self.dirtiness)
        )

    def act(self):
        self.dirtiness += 5

    def add_new_resident(self, *args):
        for object in args:
            self.residents.append(object)


class Human:

    def __init__(self, name, house):
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.name = name
        self.spouse = None

    def __str__(self):
        if self.fullness <= 0:
            return '{} has passed away because of hunger'.format(self.name)
        elif self.happiness <= 10:
            return '{} has passed away because of unhappiness'.format(self.name)
        else:
            return 'I am {}, my fullness is {}, my happiness {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.fullness += 30
            # print('{} has eaten'.format(self.name))
        else:
            self.fullness -= 10
            # print('not enough food in the house')

    def get_married(self, spouse):
        self.spouse = spouse
        spouse.spouse = self
        # print('{} married {}'.format(self.name, spouse.name))

    def pet_cat(self):
        if self.house.cat:
            self.happiness += 5
            # print('{} pet the cat'.format(self.name))
        else:
            pass
            # print('{} there is no cat in the house')

    def adopt_cat(self, cat):
        self.house.cat = cat


class Husband(Human):

    def __init__(self, name, house, salary):
        super().__init__(name, house)
        self.money_earned = 0
        self.salary = salary

    def act(self):
        if self.fullness <= 0 or self.happiness <= 10:
            return
        elif self.house.dirtiness >= 90:
            self.happiness -= 10
            # print('why is everything so dirty around here?')
        if self.fullness <= 70 and self.house.food >= 30:
            self.house.food_eaten += 30
            self.eat()
        elif self.house.money < 300:
            self.work()
        else:
            self.random_action()

    def work(self):
        if self.house.food >= 10:
            self.fullness -= 10
            self.house.money += self.salary
            # print('{} worked for the whole day'.format(self.name))
            self.money_earned += 150
        else:
            pass
            # print('I am too hungry to work')

    def random_action(self):
        if self.house.food >= 10:
            random_number = randint(1, 4)
            self.fullness -= 10
        else:
            # print('{} cant do anything while hungry'.format(self.name))
            return
        if random_number == 1:
            self.happiness += 20
            # print('{} played WoT for the whole day'.format(self.name))
        elif random_number == 2:
            self.happiness += 20
            # print('{} watched TV for the whole day'.format(self.name))
        elif random_number == 3:
            self.happiness += 20
            self.spouse.happiness += 20
            # print('{} gave flowers to his wife'.format(self.name))
        elif random_number == 4:
            self.pet_cat()


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.coats_bought = 0

    def act(self):
        if self.fullness <= 0 or self.happiness <= 10:
            return
        elif self.house.dirtiness >= 90:
            self.happiness -= 10
            # print('why is everything so dirty around here?')
        if self.fullness <= 60 and self.house.food >= 30:
            self.house.food_eaten += 30
            self.eat()
        elif self.house.food <= 60 or self.house.cat_food < 60:
            self.shopping()
        elif self.happiness <= 30:
            self.buy_fur_coat()
        elif self.house.dirtiness >= 70:
            self.clean_house()
        else:
            self.random_action()

    def shopping(self):
        if self.house.money >= 140:
            self.fullness -= 10
            self.house.money -= 140
            self.house.food += 80
            self.house.cat_food += 60
            # print('{} bought some human and cat food'.format(self.name))
        elif self.house.money >= 80:
            self.fullness -= 10
            self.house.money -= 80
            self.house.food += 60
            self.house.cat_food += 20
            # print('{} bought some food'.format(self.name))
        else:
            pass
            # print('not enough money to buy food')

    def buy_fur_coat(self):
        if self.house.food >= 10 and self.house.money >= 350:
            self.fullness -= 10
            self.house.money -= 350
            self.happiness += 60
            self.coats_bought += 1
            # print('{} bought a new coat'.format(self.name))
        else:
            if self.house.food >= 10:
                pass
                # print('not enough energy to but a new coat')
            elif self.house.money >= 350:
                pass
                # print('not enough money to but a new coat')

    def clean_house(self):
        if self.house.food >= 10:
            self.fullness -= 10
            self.house.dirtiness -= 100
            # print('{} cleaned the house'.format(self.name))
        else:
            pass
            # print('{} is too hungry to clean'.format(self.name))

    def random_action(self):
        if self.house.food >= 10:
            random_number = randint(1, 4)
            self.fullness -= 10
        else:
            # print('{} cant do anything while hungry'.format(self.name))
            return
        if random_number == 1:
            # print('{} annoyed husband for the whole day'.format(self.name))
            self.spouse.happiness -= 10
        elif random_number == 2:
            pass
            # print('{} watched TV for the whole day'.format(self.name))
        elif random_number == 3:
            # print('{} went out for the whole night '.format(self.name))
            self.house.money -= 20
        elif random_number == 4:
            self.pet_cat()


class Cat:

    def __init__(self, name, house):
        self.fullness = 30
        self.name = name
        self.house = house

    def __str__(self):
        if self.fullness <= 0:
            return '{} died because of hunger'
        else:
            return '{} fullness is {}'.format(self.name, self.fullness)

    def act(self):
        dice = randint(0, 1)
        if self.fullness <= 0:
            return
        if self.fullness <= 30:
            self.eat()
        elif dice == 0:
            self.sleep()
        elif dice == 1:
            self.scratch__wallpapers()

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            self.house.cat_food_eaten += 10
            # print('{} has eaten'.format(self.name))
        else:
            self.fullness -= 10
            # print('{} is starving'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        # print('{} slept around 20 hours'.format(self.name))

    def scratch__wallpapers(self):
        self.fullness -= 10
        self.house.dirtiness += 5
        # print('{} scratched the wallpapers'.format(self.name))


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = 100

    def act(self):
        if self.fullness <= 0:
            return
        if self.fullness <= 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 20:
            self.house.food -= 10
            self.fullness += 10
            self.house.food_eaten += 10
            # print('{} has eaten'.format(self.name))
        else:
            self.fullness -= 10
            # print('not enough food in the house')

    def sleep(self):
        self.fullness -= 10
        # print('{} slept all day'.format(self.name))


# #
# home = House()
# sergey = Husband(name='Sergey', house=home , salary=1)
# masha = Wife(name='Masha', house=home)
# barsik = Cat(name='Barsik', house=home)
# sergey.get_married(masha)
# sergey.adopt_cat(cat=barsik)
# elena = Child(name='Elena', house=home)
# home.add_new_resident(sergey, masha, barsik, elena)
#
# for day in range(1, 366):
#     cprint('================== Day {} =================='.format(day), color='red')
#     for resident in home.residents:
#         resident.act()
#     for resident in home.residents:
#         cprint(resident, color='cyan')
#     home.act()
#     cprint(home, color='cyan')

# # print('{} earned {} in total'.format(sergey.name, sergey.money_earned))
# # print(('{} food was eaten in total'.format(home.food_eaten)))
# # print(('{} bought {} coats in total'.format(masha.name, masha.coats_bought)))

# зачет третей части

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_accidents in range(6):
#   for money_accidents in range(6):
#       life = Simulation(money_accidents, food_accidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           # print('При зарплате {salary} максимально можно прокормить {max_cats} котов')


class Simulation:

    def who_survived(self, house):
        people_alive = 0
        cats_alive = 0
        for resident in house.residents:
            if isinstance(resident, Human) and resident.fullness > 0:
                people_alive += 1
            elif isinstance(resident, Cat) and resident.fullness > 0:
                cats_alive += 1
        return [cats_alive, people_alive]

    def simulate(self, amount_of_cats, salary):
        home = House()
        sergey = Husband(name='Sergey', house=home, salary=salary)
        masha = Wife(name='Masha', house=home)
        for _ in range(amount_of_cats):
            barsik = Cat(name='Barsik', house=home)
            masha.adopt_cat(cat=barsik)
            home.add_new_resident(barsik)
        sergey.get_married(masha)
        elena = Child(name='Elena', house=home)
        home.add_new_resident(sergey, masha, elena)
        for day in range(1, 366):
            for resident in home.residents:
                resident.act()
            home.act()
        return home

    def check_the_result(self, result, amount_of_cats):
        negative = 0
        positive = 0
        for run in range(3):
            if result[run] == [amount_of_cats, 3]:
                positive += 1
            else:
                negative += 1
        if positive > negative:
            return True
        else:
            return False

    def experiment(self, salary):
        for amount_of_cats in range(1, 10):
            result = []
            for run in range(1, 4):
                result.append(self.who_survived(self.simulate(amount_of_cats=amount_of_cats, salary=salary)))
            if self.check_the_result(result, amount_of_cats):
                continue
            else:
                if amount_of_cats >= 1:
                    return '{} cats can live in this family if the salary is {} '.format(amount_of_cats - 1, salary)
                if amount_of_cats == 0:
                    return '{} cats can live in this family if the salary is {} '.format(amount_of_cats, salary)


life = Simulation()
for salary in range(50, 401, 50):
    print(life.experiment(salary))


#TODO Hello Alex, I have been working on this task for the las couple of days, but I cant understand why
# the result is so strange. I've been trying to find a mistake but I could not... Would you be able
# to point me in the right direction, please?