#Dictionary views and sets
d1= dict(a=1, b=2, c=3)
print('d1',d1)
k=d1.keys()
print('keys',k)
print('list of keys',list(k))
print()
v=d1.values()
print('values',v)
print('list of values',list(v))
print()
i=d1.items()
print('items',i)
print('list of items',list(i))
print()
print('list(k)[0]',list(k)[0])
for k1 in d1.keys():
    print(k1)
print()
for v1 in d1.values():
    print(v1)
print()
for i1 in d1.items():
    print(i1)
d2={'a': 1, 'b': 2, 'c': 3}
print('d2',d2)
k3= d2.keys()
print('kyes',k3)
print('list of keys',list(k3))
v3=d2.values()
print('values',v3)
print('list of values',list(v3))
del d2['a']
print('d2',d2)
d3={'name':'raju','name2':'raju'}
print('name',d3)
