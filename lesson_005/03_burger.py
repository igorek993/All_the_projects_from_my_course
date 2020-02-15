# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger


from lesson_005 import my_burger

print('Double Cheeseburger recipe')

my_burger.add_Beef_Patty()
my_burger.add_Cheese()
my_burger.add_Regular_Bun()
my_burger.add_Pickle_Slices()
my_burger.add_Ketchup()
my_burger.add_Onions()
my_burger.add_Grill_Seasoning()
my_burger.add_Mustard()

print('My own burger recipe')

my_burger.add_Beef_Patty()
my_burger.add_Cheese()
my_burger.add_Regular_Bun()
my_burger.add_Pickle_Slices()
my_burger.add_Ketchup()
my_burger.add_Onions()
my_burger.add_chili()
my_burger.add_bbq_sauce()

# зачет!
