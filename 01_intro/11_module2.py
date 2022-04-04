import module1 as div

a, b = div.divide(2305, 29)
print (a,b)


from module1 import divide
#from module1 import *

c,d = divide(2305, 29)
print (c,d)

help(list)