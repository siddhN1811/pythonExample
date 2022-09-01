#The if/else Ternary Expression
x=0
y=2
z=3
if x:
    a=y
    print(a,y)
else:
    a=z
    print(a,z)
a=y if x else z
print(a)
b1= 't' if 'spam' else 'f'
print(b1)
b2='t' if '' else 'f'
print(b2)
