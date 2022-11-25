# # HomeWork 1. Task 5.
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

print('Найдем расстояние между двумя точками в 2D пространстве.')
xA = float(input('Введите координату точки А по оси оХ: '))
yA = float(input('Введите координату точки А по оси оY: '))
xB = float(input('Введите координату точки В по оси оХ: '))
yB = float(input('Введите координату точки В по оси оY: '))
import math
distance = round(math.sqrt((xB-xA)**2+(yB-yA)**2), 3)
print(
    f'Расстояние между точками А({xA}; {yA}) и В({xB}; {yB}) составляет {distance}')
