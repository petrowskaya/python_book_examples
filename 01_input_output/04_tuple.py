# Кортежи, списки которые нельзя изменять, предпочтительнее использовать, тк занимают меньше памяти
# Файл содержит строки вида “name,shares,price”
filename = 'input/portfolio.csv'
portfolio = []
for line in open(filename):
    fields = line.split(';') # Преобразует строку в список
    name = fields[0] # Извлекает и преобразует отдельные значения полей
    shares = int(fields[1])
    price = float(fields[2].replace(',','.'))
    stock = (name,shares,price) # Создает кортеж (name, shares, price)
    portfolio.append(stock)     # Добавляет в список записей

total = 0.0
for name, shares, price in portfolio:
    total += shares * price
print(total)