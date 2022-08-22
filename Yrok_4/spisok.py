# списки list
empty_list = []
print(type(empty_list))

empty_list1 = list()  # назначение через команду list
print(empty_list1)   # вывод списка

filled_list = [1, 23.234, True, None, 'Some string', [1, 2, 3, 4, 5,['One', 'Two', 'Three']]]
print(filled_list)
print(filled_list[0])
print(filled_list[0:7:2])  # использование индексации как и в строках
print(filled_list[-1][2])  # индексация списка в списке
print(filled_list[-1][-1][2])
print(filled_list[-1][-1][2][2])
print(filled_list[0:4])    # при выполнение среза списка на выходе получим список
print(len(filled_list))    # можно подсчитать длину списка

test_list = [1, 2, 3, 4, 5, 6]
print(test_list[1])
test_list[1] = 777         # замена одного конкретного элемента списка
print(test_list)
test_list[1] = 2
test_list[1:4] = 'SEVEN'   # при замене среза строкой, строка разбивается по индексам
print(test_list)           # [1, 'S', 'E', 'V', 'E', 'N', 5, 6]
test_list[1:4] = '555'     # заменять на чисты числа нельзя
print(test_list)
test_list[1:4] = [3, 3, 3, 3]
print(test_list)

courses = ['Histori', 'Math', 'Programming', 'Literatura', 'Physics']
numbers = [1, 6, 4, 7, 9, 11]

courses.append('Art')        # метод apeend - добавь в список ( в конец списка)
print(courses)

courses.insert(2, 'English')  # добавляет новый элемент списка нана конкретный индекс с сдвигом индексов остальных
# элемонтов списка
print(courses)

courses = ['Histori', 'Math', 'Programming', 'Literatura', 'Physics']
new_courses = ['Art', 'English']

courses.append(new_courses)    # список добавляет в виде списка
print(courses)

courses = ['Histori', 'Math', 'Programming', 'Literatura', 'Physics']
courses.extend(new_courses)    # метод extend расширяет список за счет друго списка, добавляет элементы из второго
# списка в конец списка,
print(courses)
print(len(courses))
courses.extend('Art')           # при внесении строки, строку разбивает на элементы
print(courses)
# строка, списки, кортежи, словари, множества являеются итерируемым объектом
# числа, булевы зачения, None, не являются итерируемым объектом
