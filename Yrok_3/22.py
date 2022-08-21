a = "sdfsf" \
    "sfsdf"
b = ''                # в одинарных или двойных кавычках при выполнении переноса, при выводе переноса не будет
c = """
Hello
world
planet
"""                   # при тройных кавычках сохраняется перенос
d = ''''''

print(a)
print(c)

x = 'Hello'
z = 'world'
print(x + ' ' + z)
print(x + z, 1213)    # при сложении между переменными не ставится пробел, после запятой всегда ставится пробел
print(x + z + str(12314))  # при сложениии строки и числа число всегда необходимо переводить в строку

salary = 1000
new_string = "John's salari is {}"
print(new_string.format(salary))  # заменяет {} переменной

new_string1 = "John's salari is {} {}"
print(new_string1.format(salary, True))  # при нескольких {}  скобок необходмио вносить аргумент True

user_name = "John"
new_string2 = "{1}'s salari is {0}"
print(new_string2)
print(new_string2.format(salary, user_name))  # при установке в {}  скобках регистов от 0 и ... аргументы
# format меняют согласно регистов (salari - 0 регистр, user_name - 2 регистр)

new_string3 = "{1}'s salari is {0} {2}"
print(new_string3.format(salary, user_name, 'dollars'))

new_string4 = 'This {product} costs {price} euros'
print(new_string4.format(product='computer', price=1000))

new_string5 = 'This {product} costs {price:.2f} euros'   # :.2f после price при выводе отображает сколько цены
# после точки мы хотим увидеть
print(new_string5.format(product='computer', price=1000))

s = 23042.23424
f = 29034029049.329829
print('The value  of s is %.4f' % s)
print('The value  of f is %.4f' % f)  # старый неиспользуемый метод может попасться в старых кодах

name = 'Andrey'
surname = 'Cmiit'
age = 30
print(f'Hi {name} {surname}. You are {age} yers old.')  # современный метод вывод информации с переменными, f(format)
print(f'{name + " " + surname}. Yoy are {age - 20} yers old.')  # внутри {} скобок можно также выполнять разные действия
user_name3 = f'{name + " " + surname}. Yoy are {age - 20} yers old.'  # так же можно присвоить переменной

