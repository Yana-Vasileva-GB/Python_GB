# Task 3.
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.

# # 1) При вводе положительных чисел:
# print('Выведем последовательность чисел от -N до N.')
# a = int(input('Введите число N = '))
# print(*range(-a, a+1))

# 2) При ввводе положительных и отрицательных чисел:
print('Выведем последовательность чисел от -N до N.')
a = int(input('Введите число N = '))
if a > 0:
    print(*range(-a, a+1))
else:
    print(*range(-a, a-1, -1))
