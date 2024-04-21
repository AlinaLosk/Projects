
# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
# 1. У пользователя запрашивается количество билетов
# 2. Для каждого билета запрашивается возраст посетителя:
# Если возраст менее 18 лет - проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате.
# Если человек регистрирует больше трёх человек на конференцию,то дополнительно получает 10% скидку.

tacks = int(input('Введите колличество билетов: '))
money = 0
for age in range(tacks):
    age = int(input('Введите возраст: '))
    # if age > 100 or age <= 0:
    #  raise ValueError("Тебе не может быть столько лет")
    if age < 18:
       money += 0
       print('Конференция бесплатна')
    if 18 < age <= 25:
       money += 990
       print('Сумма за билет: 990')
    if age > 25:
       money += 1390
       print('Сумма за билет: 1390')
print()
if tacks >= 3:
    discount = money * 0.9
    print('Сумма со скидкой:', int(discount))
print('Общая сумма:', int(money))