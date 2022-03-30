### Генератор yield

def countdown(n):
    print('Обратный отсчет!')
    while n > 0:
        yield n # Генерирует значение (n)
        n -= 1

c = countdown(5)
print(c.__next__())
print(c.__next__())
print(c.__next__())

for i in countdown(5):
    print(i,end=' ')
print()
print('------------------------------------------')

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

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line
'''
f=open('input/file_tile.txt','r')

for i in tail(f):
    print(i)

for i in grep(f,'2'):
    print(i)
'''

# Реализация последовательности команд “tail -f | grep python”
# на языке Python
wwwlog = tail(open('input/access-log'))
pylines = grep(wwwlog,'python')
for line in pylines:
    print(line,end=' ')

