import datetime

now = datetime.datetime.today()
print ('Format date time: {:02d}-{:02d}-{:04d} {:02d}:{:02d}:{:02d}'.format(now.day,now.month,now.year,now.hour,now.minute,now.second))
print ('Format date time new: %02d-%02d-%04d %02d:%02d:%02d' % (now.day,now.month,now.year,now.hour,now.minute,now.second))

def min(a):
    # Ничего не делать
    pass

principal = 1000 # Начальная сумма вклада
rate = 0.05 # Процент
numyears = 5 # Количество лет
year = 1

f = open('data/out','w') # Открывает файл для записи
while year <= numyears:
    principal = principal * (1 + rate)
    f.write('%3d %0.2f' % (year,principal))
    print ('%3d %0.2f' % (year,principal))
    #print ( f,'%3d %0.2f' % (year,principal))
    year += 1
f.close()