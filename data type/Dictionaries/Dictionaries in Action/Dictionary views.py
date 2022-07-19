#Dictionary views
d1= dict(a=1, b=2, c=3)
print(d1)
print('keys',d1.keys())
print('keys',list(d1.keys()))
print('values',d1.values())
print('values',list(d1.values()))
print('item',d1.items())
print('item',dict(list(d1.items())))
