"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
import random
def my_func(*args):
    result = []
    for i in range(1, len(tmp_list)):
        if tmp_list[i] > tmp_list[i - 1]:
            result.append(tmp_list[i])
    return result
tmp_list = random.sample(range(50, 500), 10)
print(tmp_list)
new_list = [int(i) for i in my_func(tmp_list)]
print (new_list)
