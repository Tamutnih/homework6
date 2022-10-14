# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2]))

# Второе решение
# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")


# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_odd_index(lst)


# Решение 3
# lst = [2, 3, 5, 9, 3]
# # def f(x): return (sum[1::2])
# sum_odd = sum(lst[item] for item in range(1, len(lst), 2))
# odd_el = str([lst[item]
#              for item in range(1, len(lst), 2)]).strip('[]')
# print(
#     f'Для списка {lst} сумма чисел, стоящих на нечётных позициях: \n{odd_el} = {sum_odd}.')
