# работа со строками
string_sample = 'Hello world world'
#                0123456789.......
#     .....-8,-7,-6,-5,-4,-3,-2,-1
string_sample2 = 'first letteR is lowErcase'
string_sample3 = 'extra whitespace string '
german_sample = 'der FluB'
# sfsd s dfdsfdfhdfhd fdyhredg индексация
print(string_sample[4])
print(string_sample[0:5])     #
print(string_sample[-1])
print(string_sample[-5:-1])   # от -5 индекса до конца (word)
print(string_sample[-5:])     # от -5 индекса до конца (word)
print(string_sample[:10])     #
print(string_sample[6:11])    # внутри print временная, не меняет переменную
print(string_sample[::-1])    # c шагом -1 строка выводится наоборот

# [START:END:STEP] STEP (шаг) по умолчанию 1

print(string_sample[6:10:2])  # с шагом 2

# подсчет длины строки

print(len(string_sample))
print(len('12124234'), 12124576)  # при подсчета количество символов числа int необходимо конвертировать в строку str

print("World" in string_sample)
print("world" in string_sample)   # проверка на наличие в переменной
print(string_sample in "world")   # проверяет переменную в строке результат False
print(string_sample in "Hello world world")  # проверяет переменную в строке результат True
print('A' == 'a')                # пайтон чуствителен на регистр результат False

print(string_sample2)
print(type(len('Hello world')))
print(string_sample2.upper())    # возведение в верхний регистр

print(german_sample)
print(german_sample.lower())      # выводит всю строку в нижнем регистре
print(german_sample.casefold())   # выводит всю строку в нижнем регистре кроме символов не имеющих аналогов
# в нижнем регистре (немецкий, греческий и тд.)

print(german_sample.capitalize())  # выводит первый символ строки с верхний регистр
# метод strip    не меняет переменную
print('Hello', end='***')          # при выводе на печать end убирает перенос на новую строку и добавляет ***
print('word')
print(string_sample3.strip())      # метод strip без аргументов() убирает пробелы в начале и в конце строки
string_sample4 = '*****kljsad lks***ajd ***kkllkj ad*****'
print(string_sample4.strip('*'))    # убирает символы указанные в аргументе() в начале и концк строки если перед ними
# в начале строки или после них в конце строки нет пробела
print(string_sample4.lstrip('*'))   # убирает символы указанные в аргументе в начале строки если нет перед ними пробелов
print(string_sample4.rstrip('*'))   # тоже самое только справа

print(string_sample.replace('world', 'planet'))  # заменяет все совпадения внутри строки
print(string_sample.replace('world', 'planet', 1))  # тоже самое но аргумент 1  - количество замен

print(string_sample.lower().strip('h').replace('world', 'planet', 1))  # выполняет последовательно слева на право

print(string_sample.count('world'))  # подсчитывает количество совпадений в строке
print(string_sample.count('world', 10, 20))  # тоже самое только с 10 до 20 индекс

print(string_sample.find('world'))   # находит первое совпадение (указывает первый регистр)
print(string_sample.find('world', 7, 20))  # находит первое совпадение на участв\ке с 8 по 20 индексы
