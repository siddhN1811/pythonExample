# set operator
x={1,2,3,4,5,6}
y={4,5,6,8,9,10}
z={'raju'}
w={'siddhanth'}
print('x={1,2,3,4,5,6} y={4,5,6,8,9,10}')
print('union',x | y |z |w)
print('union',x.union(y,z,w))
print('union',x.union({11,12,13,14,78}))
print('union',x|{7,8,9})
print('intersection',x & y)
print('intersection',x.intersection(y))
print('set difference x-y',x-y)
print('set difference y-x',y-x)
print('symm difference x-y',x^y)
x.add(12)
print('add 12 in x',x)
x.remove(12)
print('remove 12 from x',x)
print('5 in x',5 in x)
print('range',x.issubset({1,2,3,9}))
print('subset',z<x)
print('superset',x>z)
print('w',w)
print('length of set x:',len(x))
print('length of set y:',len(y))
print('length of set z:',len(z))
