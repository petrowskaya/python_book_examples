# возвратить несколько значений
def divide(a, b):
    q = a // b # Если a и b – целые числа, q будет целым числом
    r = a - q*b
    return (q,r)

quotient, remainder = divide(1456, 33)
print('quotient={}, remainder={}'.format(quotient, remainder))

# пример генератора yield

