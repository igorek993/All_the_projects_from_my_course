# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
days_amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month <= 12:
    print(days_amount[month - 1])
else:
    print('This month does not exist')

# This looks a way better than it was before, thank you!

# зачет!
