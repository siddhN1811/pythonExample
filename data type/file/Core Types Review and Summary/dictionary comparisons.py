# dictionary comparisons
d1= {'a':1, 'b':2}
d2= {'a':1, 'b':3}
l1=sorted(d1.items())
print(l1)
l2=sorted(d2.items())
print(l2)
print(l1<l2)
print(l2<l1)
