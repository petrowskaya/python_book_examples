import datetime

now = datetime.datetime.today()
print ('Format date time: {:02d}-{:02d}-{:04d} {:02d}:{:02d}:{:02d}'.format(now.day,now.month,now.year,now.hour,now.minute,now.second))
print ('Format date time new: %02d-%02d-%04d %02d:%02d:%02d' % (now.day,now.month,now.year,now.hour,now.minute,now.second))

def min(a):
    pass # Ничего не делать

principal = 1000 # Начальная сумма вклада
rate = 0.05 # Процент
numyears = 5 # Количество лет
year = 1

f = open('output/out','w') # Открывает файл для записи
while year <= numyears:
    principal = principal * (1 + rate)
    print ('%3d %0.2f' % (year,principal))
    #print ('%3d %0.2f' % (year,principal),file=f)
    f.write('%3d %0.2f\n' % (year,principal))
    year += 1
f.close()

x = 37
s1 = 'Значение переменной x: ' + str(x)
s2 = 'Значение переменной x: ' + repr(x)
s3 = 'Значение переменной x: ' + format(x,'4d')

print ('%s %s %s' %(s1,s2,s3))

'''
name = input('Введите свое имя : ')
print ('%s, добрый день!'% name)
'''

