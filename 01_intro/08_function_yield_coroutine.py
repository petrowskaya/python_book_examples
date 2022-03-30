# функция: поиск подстроки matchtext
def print_matches(matchtext):
    print('Поиск подстроки:', matchtext)
    while True:
        line = (yield) # Получение текстовой строки
        if matchtext in line:
            print(line,end='')
'''
matcher = print_matches('python')
matcher.__next__() # Перемещение до первой инструкции (yield)
#Поиск подстроки python
matcher.send('Hello World')
matcher.send('python is cool')
matcher.send('yow!')
matcher.close() # Завершение работы с объектом matcher
'''
# следит за содержимым файла (на манер команды tail -f)
import time

def tail(f):
    f.seek(0,2) # Переход в конец файла

    while True:
        line = f.readline() # Попытаться прочитать новую строку текста
        if not line: # Если ничего не прочитано,
            time.sleep(0.1) # приостановиться на короткое время
            continue # и повторить попытку
        yield line

# Множество сопрограмм поиска
matchers = [
    print_matches('python'),
    print_matches('guido'),
    print_matches('jython')
]

# Подготовка всех подпрограмм к последующему вызову метода next()
for m in matchers: m.__next__()

# Передать активный файл журнала всем сопрограммам.
# Обратите внимание: для нормальной работы необходимо,
# чтобы веб-сервер активно записывал данные в журнал.
wwwlog = tail(open('input/access-log'))
for line in wwwlog:
    for m in matchers:
        m.send(line) # Передача данных каждой из сопрограмм