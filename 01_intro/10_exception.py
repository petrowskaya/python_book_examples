try:
    f = open('file.txt','r')
except IOError as e:
    print(e)

raise RuntimeError('Компьютер говорит нет')