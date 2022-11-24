# Task 5.
# Напишите программу, которая принимает на вход число и
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# 20 - yes
# 70 - yes
# 90 - no

number = int(
    input('Проверим кратность числа на 5 и 10 или 15, но не 30.\nВведите число: '))
if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and not (number % 30 == 0):
    print('True')
else:
    print('False')
