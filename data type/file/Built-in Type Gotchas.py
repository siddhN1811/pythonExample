#Built-in Type Gotchas
l1=[1,2,3]
print(l1)
x1=l1*2
print(x1)
y1=[l1]*2
print(y1)
l1[1]=4
print(l1,x1,y1)
print()
l2=[4,5,6]
y2=[list(l2)]*4
print('l2',l2,'y2',y2)
l2[1]=8
print('l2',l2,'y2',y2)
y2[0][1] = 99
print('y2',y2)
print()
l3 = [4, 5, 6]
y3 = [list(l3) for i in range(4)]
print('l3',l3,'y3',y3)
y3[0][1] = 99
print('l3',l3,'y3',y3)
