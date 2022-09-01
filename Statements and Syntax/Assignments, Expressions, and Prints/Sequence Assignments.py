#Sequence Assignments
[a, b, c] = (1, 2, 3)
print([a,b,c])
string='spam'
a,b ,c,d=string
print((a,b,c,d))
a, b, c = string[0], string[1], string[2:]
print((a,b,c))
a, b, c = list(string[:2]) + [string[2:]]
print((a,b,c))
(a, b), c = string[:2], string[2:]
print('Nested sequences',(a,b,c))
((a, b), c) = ('SP', 'AM')
print('Paired by shape and position',(a,b,c))
L = [1, 2, 3, 4]
while L:
    f,L=L[0],L[1:]
    print(f,L)


