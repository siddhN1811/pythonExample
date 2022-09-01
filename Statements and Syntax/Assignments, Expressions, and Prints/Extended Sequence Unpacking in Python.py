#Extended Sequence Unpacking in Python 3.X
L = [1, 2, 3, 4]
while L:
    f,*L=L
    print(f,L)
seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a,b,c,d)
a, b, c, d,*e = seq
print(a,b,c,d,e)
a, b, *e, c, d = seq
print(a, b, e,c, d)
[*a]=seq
print(a)
