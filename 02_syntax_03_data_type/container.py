# list - tuple - dictionary
# список - кортеж - словарь 
a = [ 1, 3.4, 'hello' ] # Список
b = ( 10, 20, 30 ) # Кортеж
c = { 'a': 3, 'b': 42 } # Словарь



# пример грамотного разбора строки в список по типам
line = 'GOOG,100,490.10'
field_types = [str, int, float]
raw_fields = line.split(',')
fields = [ty(val) for ty,val in zip(field_types,raw_fields)]
print(fields)

# пример использования строки документирования
def new_func():
    "пустая функция - а это строка документирования"
    pass

print(new_func.__doc__)

# сравнение объектов
if type(a) is list: print('a list')
if isinstance(c,dict): print('c dict')

