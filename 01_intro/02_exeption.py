
content = ''
suffix = '.ht'
if suffix == '.htm':
    content = 'text/html'
elif suffix == '.jpg':
    content = 'image/jpeg'
elif suffix == '.png':
    content = 'image/png'
else:
    content = 'none'
    raise RuntimeError('Содержимое неизвестного типа')

print(content)