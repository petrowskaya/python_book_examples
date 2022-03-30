names = [ 'Dave', 'Mark', 'Ann', 'Phil' ]
names.append('Paula')
names.insert(2, 'Thomas')
print(names)

b = names[0:2] # Вернет ['Jeff', 'Mark']
print(b)
c = names[2:] # Вернет ['Thomas', 'Ann', 'Phil', 'Paula']
print(c)
names[1] = 'Jeff' # Во второй элемент запишет имя 'Jeff'
print(names)
names[0:2] = ['Dave','Mark','Jeff'] # Заменит первые два элемента списком справа.
print(names)

#-------------------------------------------
a = [1,'Dave',3.14, ['Mark', 7, 9, [100,101]], 10]
print(a[1]) # Вернет 'Dave'
print(a[3][2]) # Вернет 9
print(a[3][3][1]) # Вернет 101


