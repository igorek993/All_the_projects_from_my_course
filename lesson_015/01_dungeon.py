# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# — Монстра Mob_exp10_tm0
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...


# если изначально не писать число в виде строки - теряется точность!
import datetime
from collections import defaultdict

field_names = ['current_location', 'current_experience', 'current_date']

# Учитывая время и опыт, не забывайте о точности вычислений!
import json, re, decimal


class Game:

    def __init__(self):
        self.current_dungeon = None
        self.current_exp = 0
        self.remaining_time = decimal.Decimal('123456.0987654321')
        self.time_in_game = datetime.timedelta(seconds=0)
        self.dungeon_levels = defaultdict(list)
        self.current_location = None
        self.current_monsters = list()
        self.time_pattern = f'tm\S*'
        self.current_dungeons = list()

    def open_dungeon_json(self):
        with open('rpg.json', 'r') as read_file:
            dungeon = json.load(read_file)
            return dungeon

    def print_next_round(self):
        print(
            f'You are in {self.current_dungeon}\nYou have {self.current_exp} experience and'
            f' {self.remaining_time} seconds left before flooding\nTime passed in the dungeon: {self.time_in_game}\n'
            f'\nYou can see the following around you:')

    def print_choice(self):
        print('\nMake your choice:\n1.Attack a monster\n2.Enter a dungeon\n3.Give up and run away like a chicken')
        return int(input())

    def remaining_time_counter(self, _object):
        if isinstance(_object, dict):
            time_spent = (re.search(self.time_pattern, ''.join(list(_object.keys()))).group())[2:]
            self.remaining_time = self.remaining_time - decimal.Decimal(time_spent)
            if self.remaining_time <= 0:
                print('Death text here')
        elif isinstance(_object, str):
            time_spent = (re.search(self.time_pattern, ''.join(_object)).group())[2:]
            self.remaining_time = self.remaining_time - decimal.Decimal(time_spent)

    def time_in_game_counter(self, _object):
        if isinstance(_object, dict):
            time_spent = (re.search(self.time_pattern, ''.join(list(_object.keys()))).group())[2:]
            self.time_in_game = self.time_in_game + datetime.timedelta(seconds=int(time_spent))
        elif isinstance(_object, str):
            time_spent = (re.search(self.time_pattern, ''.join(_object)).group())[2:]
            self.time_in_game = self.time_in_game + datetime.timedelta(seconds=int(time_spent))

    def time_counter(self, _object):
        self.time_in_game_counter(_object)
        self.remaining_time_counter(_object)

    def print_after_fight(self, monster):
        print(
            f'You fought {monster}\nYou are in {self.current_dungeon}\n'
            f'You have {self.current_exp} experience and you have {self.remaining_time} seconds left before '
            f'flooding\nTime passed in the dungeon: {self.time_in_game}\n')

    def fight_a_monster(self):
        while True:
            if not self.current_monsters:
                print('There is no monster to fight!')
            print('You decided to fight a monster\n')
            if len(self.current_monsters) >= 2:
                print(f'What monster are you gonna fight?\n')
                counter = 1
                for monster in self.current_monsters:
                    print(f'{counter}.{monster}')
                    counter += 1
                monster_number = int(input()) - 1
                monster_to_fight = self.current_monsters[monster_number]
                self.current_monsters.pop(monster_number - 1)
                self.time_counter(monster_to_fight)
                self.print_after_fight(monster_to_fight)
                print(
                    f'Would you like to fight another monster or make your way deeper into the dungeon?\n1. I am ready '
                    f'for another fight\n2. Move forward')
                choice = int(input())
                if choice == 1:
                    pass
                if choice == 2:
                    for dungeon in self.current_dungeons:
                        print(f'{counter}. {str().join(list(dungeon.keys()))}')
                        counter += 1
                        return int(input()) - 1
            elif len(self.current_monsters) == 1:
                self.time_counter(self.current_monsters[0])
                self.print_after_fight(self.current_monsters[0])
                self.current_monsters.remove(self.current_monsters[0])
                print('There are no monsters left, please choose where you would like to go')
                counter = 1
                for dungeon in self.current_dungeons:
                    print(f'{counter}. {str().join(list(dungeon.keys()))}')
                    counter += 1
                print(int(input()) - 1, '!!!!')
                return int(input()) - 1

    def print_post_choice(self, choice, dungeon):
        if choice == 1:
            return self.fight_a_monster()
        elif choice == 2:
            print(f'You are entering location {self.current_dungeon}\n')
            self.time_counter(dungeon)
        elif choice == 3:
            print('You are not strong enough for this challenge, come back when you are ready!\n')

    def find_next_level(self, dungeon):
        while True:
            for key, value in dungeon.items():
                self.current_monsters = list()
                self.current_dungeons = list()
                self.current_dungeon = key
                self.print_next_round()
                for i in value:
                    if isinstance(i, str):
                        print('- Monster', i)
                        self.current_monsters.append(i)
                    if isinstance(i, dict):
                        self.current_dungeons.append(i)
                        print('- Dungeon entrance', ''.join(list(i.keys())))
                choice = self.print_choice()
                dungeon = dungeon[key][choice]  # TODO change the order so 'choice' changes after the choice
                self.print_post_choice(choice, dungeon)

    def run(self):
        self.find_next_level(self.open_dungeon_json())


test = Game()

test.run()
