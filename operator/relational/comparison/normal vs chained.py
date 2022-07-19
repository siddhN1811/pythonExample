# normal vs chained
x=10
y=45
z=30
w=40
print('normal x=10 y=20')
print('less than',x<y and y<z)
print('chained')
print('less tahn y',x<y<z)
print('and ',x<y>z<w)
print('or',(x<y)+(y>z<w)) # might be used in crypto
print('1==2<3',1==2<3)
