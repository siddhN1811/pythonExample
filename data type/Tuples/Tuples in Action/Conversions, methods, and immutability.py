#Conversions, methods, and immutability
t1= ('cc', 'aa', 'dd', 'bb')
temp=list(t1)
temp.sort()
print('sorted',temp)
t2=('cc', 'aa', 'dd', 'bb')
print(sorted(tuple(t2)))
t3= (1, 2, 3, 4, 5)
l1= [x + 20 for x in t3]
print('list',l1)
t4=(1, 2, 3, 2, 4, 2)
print('tuple',t4)
print(' T.index(2)', t4.index(2))
print(' T.index(2, 2)', t4.index(2,2))
print(' T.index(2,2)', t4.index(2,4))
print('count',t4.count(2))
t5= ('raju', ['python','java','c#'], 'dev')
t5[0]='mane'
print('t5',t5[1])
