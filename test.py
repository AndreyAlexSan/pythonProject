# площадь треугольника
a = float(input('сторона А: '))
b = float(input('сторона В: '))
c = float(input('сторона С: '))

hafl_p = (a + b + c) / 2

print('полупериметр = ', hafl_p)

area: float = (hafl_p*(hafl_p-a)*(hafl_p-b)*(hafl_p-c))**0.5

print('площадь трегуольника равна ', area)