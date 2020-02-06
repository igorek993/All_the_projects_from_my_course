# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
yearly_expenses = 12000
monthly_expenses_current = 12000
count = 0
while count < 9:
    # monthly_expenses_current = (monthly_expenses_current + (monthly_expenses_current * 0.03))
    monthly_expenses_current *= 1.03  # the same calculation but a bit shorter
    # I thought I did include the inflation rate correctly by excluding the very first month from the loop.
    yearly_expenses += monthly_expenses_current
    count += 1

money_needed = yearly_expenses - 100000
print('Студенту надо попросить', round(money_needed, 2), 'рублей')

# зачет!
