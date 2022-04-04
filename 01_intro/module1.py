# файл : div.py
def divide(a, b):
    q = a/b # Если a и b – целые числа, q будет целым числом
    r = a - q*b
    return (q, r)

