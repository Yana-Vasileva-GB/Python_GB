# Seminar 2. Task 1
# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
# 5 => 1, -3, 9, -27, 81

number = int(input('Выведем последовательность. Введите число - '))
result = 1
for i in range(number):
    print(result, end=', ')
    result *= -3