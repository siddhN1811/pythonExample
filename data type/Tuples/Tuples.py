#Tuples
t1=()
print('An empty tuple',t1)
t2= 0,
print('A one-item tuple (not an expression)',type(t2))
t3= (0, 'Ni', 1.2, 3)
print('four item tuple',t3)
t4= 0, 'Ni', 1.2, 3
print('four item tuple',t4)
t5= ('Bob', ('dev', 'mgr'))
print('Nested tuples',t5)
t6=  tuple('spam')
print('Tuple of items in an iterable',t6)

