#More Dictionary Methods
d1={'spam': 2, 'ham': 1, 'eggs': 3}
d2= {'toast':4, 'eggs':5}
print('keys',d1.keys(),list(d1.keys()))
print('values',d1.values(),list(d1.values()))
print('items',d1.items(),list(d1.items()))
print('get',d1.get('spam'))
print('get',d1.get('toast'))
print('get',d1.get('toast', 88))
d1.update(d2)
print('d1',d1)
d1.pop('toast')
print('d1',d1)

