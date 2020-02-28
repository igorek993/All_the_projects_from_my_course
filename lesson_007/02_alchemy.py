# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
# print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return 'water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, SmallCat):
            return 'wet kitty'


class Air:
    def __str__(self):
        return 'air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Thunder()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()


class Fire:
    def __str__(self):
        return 'fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Thunder()
        elif isinstance(other, SmallCat):
            return 'no more myau'


class Earth:
    def __str__(self):
        return 'earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Storm:
    def __str__(self):
        return 'storm'

    def __add__(self, other):
        return None


class Steam:
    def __str__(self):
        return 'steam'

    def __add__(self, other):
        return None


class Dirt:
    def __str__(self):
        return 'dirt'

    def __add__(self, other):
        return None


class Thunder:
    def __str__(self):
        return 'thunder'

    def __add__(self, other):
        return None


class Dust:
    def __str__(self):
        return 'dust'

    def __add__(self, other):
        return None


class Lava:
    def __str__(self):
        return 'lava'

    def __add__(self, other):
        return None


class SmallCat:
    def __str__(self):
        return 'a small cat'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'wet kitty'
        elif isinstance(other, Fire):
            return 'no more myau'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', SmallCat(), '=', Water() + SmallCat())
print(Fire(), '+', SmallCat(), '=', Fire() + SmallCat())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
