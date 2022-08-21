# байтовая строка - это строка которая содержит в себе символы кода или какой нибудь кодировки
byte_string = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_string.decode('utf-16'))  # раскодирование байтовой строки в скобках кодировка utf-8 b utf-16 самые ходовые
#  кодировки

new_string6 = "Jhon Smith"
print(new_string6.encode('utf-16'))  # закодирование