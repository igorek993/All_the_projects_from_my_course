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
import datetime, sys
from pprint import pprint
import json, re, decimal
from colorama import Fore, Style
from collections import defaultdict

field_names = ['current_location', 'current_experience', 'current_date']


# Учитывая время и опыт, не забывайте о точности вычислений!


class Game:

    def __init__(self):
        self.current_dungeon = None
        self.CURRENT_EXP = 0
        self.REMAINING_TIME = decimal.Decimal('123456.0987654321')
        self.TIME_IN_GAME = datetime.timedelta(seconds=0)
        self.dungeon_levels = defaultdict(list)
        self.current_location = None
        self.current_monsters = list()
        self.TIME_PATTERN = r'tm\S*'
        self.EXP_PATTERN = r'exp\d{0,3}'
        self.current_dungeons = list()

    def open_dungeon_json(self):
        with open('rpg.json', 'r') as read_file:
            dungeon = json.load(read_file)
            return dungeon

    def print_next_round(self):
        print(
            f'You are in {self.current_dungeon}\nYou have {self.CURRENT_EXP} experience and'
            f' {self.REMAINING_TIME} seconds left before flooding\nTime passed in the dungeon: {self.TIME_IN_GAME}\n'
            f'\n{Fore.GREEN}You can see the following around you:{Style.RESET_ALL}')

    def remaining_time_counter(self, _object):
        if isinstance(_object, dict):
            time_spent = (re.search(self.TIME_PATTERN, ''.join(list(_object.keys()))).group())[2:]
            self.REMAINING_TIME = self.REMAINING_TIME - decimal.Decimal(time_spent)
            if self.REMAINING_TIME <= 0:
                print('Death text here')
        elif isinstance(_object, str):
            time_spent = (re.search(self.TIME_PATTERN, ''.join(_object)).group())[2:]
            self.REMAINING_TIME = self.REMAINING_TIME - decimal.Decimal(time_spent)

    def time_in_game_counter(self, _object):
        if isinstance(_object, dict):
            time_spent = (re.search(self.TIME_PATTERN, ''.join(list(_object.keys()))).group())[2:]
            self.TIME_IN_GAME = self.TIME_IN_GAME + datetime.timedelta(seconds=float(time_spent))
        elif isinstance(_object, str):
            time_spent = (re.search(self.TIME_PATTERN, ''.join(_object)).group())[2:]
            self.TIME_IN_GAME = self.TIME_IN_GAME + datetime.timedelta(seconds=float(time_spent))

    def exp_counter(self, mob):
        if isinstance(mob, str):
            exp = int(re.search(self.EXP_PATTERN, mob).group()[3:])
            self.CURRENT_EXP += exp

    def time_counter(self, _object):
        self.time_in_game_counter(_object)
        self.remaining_time_counter(_object)
        if self.game_end_check():
            return True

    def print_after_fight(self, monster):
        print(
            f'You fought {monster}\nYou are in {self.current_dungeon}\n'
            f'You have {self.CURRENT_EXP} experience and you have {self.REMAINING_TIME} seconds left before '
            f'flooding\nTime passed in the dungeon: {self.TIME_IN_GAME}\n')

    def fight_or_move(self, dungeon):
        print(
            f'Would you like to fight another monster or make your way deeper into the dungeon?\n1. I am ready '
            f'for another fight\n2. Move forward')
        choice = int(input())
        if choice == 1:
            pass
        if choice == 2:
            print(f'{Fore.LIGHTBLUE_EX}Please, choose where you would like to go{Style.RESET_ALL}')
            return self.choose_dungeon(dungeon)

    def find_monster_to_figt(self):
        print(f'What monster are you gonna fight?\n')
        counter = 1
        for monster in self.current_monsters:
            print(f'{Fore.RED}{counter}.{monster}{Style.RESET_ALL}')
            counter += 1
        return int(input()) - 1

    def fight_a_monster(self, dungeon):
        while True:
            if not self.current_monsters:
                print('There are no monsters to fight, please choose where you would like to go')
                return self.choose_dungeon(dungeon)
            print('You decided to fight a monster\n')
            if len(self.current_monsters) >= 2:
                monster_number = self.find_monster_to_figt()
                monster_to_fight = self.current_monsters[monster_number]
                self.exp_counter(monster_to_fight)
                self.current_monsters.pop(monster_number - 1)
                self.time_counter(monster_to_fight)
                self.print_after_fight(monster_to_fight)
                next_action = self.fight_or_move(dungeon)
                if next_action:
                    return next_action
                else:
                    pass
            elif len(self.current_monsters) == 1:
                return self.fight_last_monster(dungeon)

    def fight_last_monster(self, dungeon):
        self.time_counter(self.current_monsters[0])
        self.exp_counter(self.current_monsters[0])
        self.print_after_fight(self.current_monsters[0])
        self.current_monsters.remove(self.current_monsters[0])
        print('There are no monsters left, please choose where you would like to go')
        return self.choose_dungeon(dungeon)

    def choose_dungeon(self, dungeon):
        counter = 1
        real_dungeons_index = defaultdict()
        for dun in dungeon:
            if isinstance(dun, dict):
                print(f'{Fore.LIGHTBLUE_EX}{counter}. {str().join(list(dun.keys()))}{Style.RESET_ALL}')
                real_dungeons_index[counter] = dungeon.index(dun)
                counter += 1
        if not self.current_dungeons:
            return 'end'
        return real_dungeons_index[int(input())]

    def print_choice(self, dungeon):
        print(
            f'\n{Fore.GREEN}Make your choice:{Style.RESET_ALL}\n{Fore.YELLOW}1.Attack a monster\n2.Enter a '
            f'dungeon\n3.Give up and run away like a chicken{Style.RESET_ALL}')
        choice = int(input())
        if choice == 1:
            return self.fight_a_monster(dungeon)
        elif choice == 2:
            print('Choose your way wisely')
            return self.choose_dungeon(dungeon)
        elif choice == 3:
            print('You are not strong enough for this challenge, come back when you are ready!\n')
            sys.exit()

    def print_mobs_dungeons(self, value):
        for i in value:
            if isinstance(i, str):
                print(f'{Fore.RED}- Monster {i}{Style.RESET_ALL}')
                self.current_monsters.append(i)
            if isinstance(i, dict):
                self.current_dungeons.append(i)
                print(f"{Fore.LIGHTBLUE_EX}- Dungeon entrance {''.join(list(i.keys()))}")

    def reset_stat(self):
        self.REMAINING_TIME = decimal.Decimal('123456.0987654321')
        self.CURRENT_EXP = 0
        self.TIME_IN_GAME = datetime.timedelta(seconds=0)

    def game_end_check(self, option='option'):
        if option == 'end':
            print(
                f'\n{Fore.LIGHTRED_EX}You got to a point where you can not find any other entrance and there is no way '
                f'back because \nall '
                f'the other dungeons have already been flooded. You start feeling the breath of death slowly\n'
                f'approaching towards your feet, you close your eyes trying to anticipate the amount of time left\n'
                f'for you before you will not be able to breathe ever again... \nHold on! What is it? Is it some'
                f'kind of miracle? For some mysterious reason you open your eyes and see \nthe same dungeon entrance,'
                f'again! You slowly walk into this dungeon and hear water filling up the first room again... \n'
                f'it is time to keep going if you do not wanna end up like the last time!{Style.RESET_ALL}\n')
            self.reset_stat()
            return True
        elif float(self.REMAINING_TIME) < 0:
            print(
                f"{Fore.LIGHTRED_EX}It seems like you have been awake for so long that you can't move on and you have "
                f"to rest\n "
                f"for a while, you put your head on the ground and close your eyes. While sleeping, you realise\n that "
                f"there is too much water coming out of everywhere so you get up, try to escape this room\n but it's "
                f"too late now and the water is getting closer and closer to your neck.\n You close your eyes for the "
                f"last time thinking of everything you could have done if you did not get into this dungeon..."
                f"\nHold on! What is it? Is it some"
                f"kind of miracle? For some mysterious reason you open your eyes and see \nthe same dungeon entrance,"
                f"again! You slowly walk into this dungeon and hear water filling up the first room again... \n"
                f"it is time to keep going if you do not wanna end up like the last time!\n{Style.RESET_ALL}")
            self.reset_stat()
            return True
        elif 'Hatch_tm159.098765432' == self.current_dungeon:
            print(f"{Fore.YELLOW}You've found a hatch! You can see the light coming out from the other side and you "
                  f"fresh "
                  f"air blowing into your face!\n Should you try to open it up? Do you think you are powerful "
                  f"enough? \nYes/No{Style.RESET_ALL}")
            choice = input()
            if choice == 'Yes' or choice == 'yes':
                if self.CURRENT_EXP < 280:
                    print(f'{Fore.LIGHTRED_EX}You are trying to open up the hatch and finally get out from '
                          f'this dungeon. However, you '
                          f'feel that you did not gain enough power and experience during this\n journey so you can not '
                          f'lift the lid, it is too heavy for you! You start feeling the breath of death slowly\n'
                          f'approaching towards your feet, you close your eyes trying to anticipate the amount of '
                          f'time left\n '
                          f'for you before you will not be able to breathe ever again... \nHold on! What is it? Is it '
                          f'some '
                          f'kind of miracle? For some mysterious reason you open your eyes and see \nthe same dungeon '
                          f'entrance, '
                          f'again! You slowly walk into this dungeon and hear water filling up the first room '
                          f'again... \n '
                          f'it is time to keep going if you do not wanna end up like the last time!{Style.RESET_ALL}\n')
                    self.reset_stat()
                    return True
                elif self.CURRENT_EXP >= 280:
                    print(f'{Fore.YELLOW}You managed to open up the hatch and get out from this dungeon! '
                          f'Congratulations!{Style.RESET_ALL}')
                    sys.exit()
            elif choice == 'No' or choice == 'no':
                print(f'{Fore.YELLOW}You decided to keep the hatch closed and stay in the dungeon forever... '
                      f'(Why Would you choose '
                      f'it?){Style.RESET_ALL}')
                sys.exit()

    def find_next_level(self, dungeon):
        while True:
            for key, value in dungeon.items():
                self.current_monsters = list()
                self.current_dungeons = list()
                self.current_dungeon = key
                if self.time_counter(key):
                    return
                self.print_next_round()
                self.print_mobs_dungeons(value)
                choice = self.print_choice(dungeon[key])
                if self.game_end_check(option=choice):
                    return
                dungeon = dungeon[key][choice]

    def run(self):
        while True:
            self.find_next_level(self.open_dungeon_json())


test = Game()

test.run()
