# # Task 4.
# Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.
# 6,78 - 7
# 0,34 - 3
# 5 - no

number = float(input('Определим первую цифру дробной части числа.\nВведите число: '))
print(int(number * 10 % 10))
