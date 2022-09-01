#Block Delimiters: Indentation Rules
x=1
if x:
    y=2
    if y:
        z=3
        if z:
            w=4
            print(w)
        print(z)
    print(y)
print(x)
# wrong indented
x='spam'
if 'rubbery' in 'shrubbery':
 print(x * 8)
 x += 'NI'
 if x.endswith('NI'):
     x *= 2
     print(x)
