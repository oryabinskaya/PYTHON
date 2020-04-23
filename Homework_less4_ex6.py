"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count
user = int(input("Введите первое число списка: "))
for i in count(user):
    print(i)

from itertools import cycle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in cycle(my_list):
    print(i)