#for loops
for x in [1,2,3]:
    print(x, end=' ')

print('list')    
sum=0
for i in [1,2,3,4]:
    sum +=i
print('sum',sum)
print()
prod=1
for i in [1,2,3,4]:
    prod *=i
print(prod)

print('string')
name='raju'
for i in name:
    print(i,end=' ')
print('tuple')
t='raju','ramchandra','mane'
for i in t:
    print(i,end=' ')
print()
t1=[(1,2),(3,4),(5,6)]
for (a,b) in t1:
    print(a,b)

print('Dic')
d1= {'a': 1, 'b': 2, 'c': 3}
for key in d1:
    print(key,'=>',d1[key])
print()
for (key,value) in d1.items():
    print(key,'=>',value)
print()
t3=[(1, 2), (3, 4), (5, 6)]
for both in t3:
    a,b=both
    print(a,b)
print()
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)
print()
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)
print()
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
     print(a, b, c)
