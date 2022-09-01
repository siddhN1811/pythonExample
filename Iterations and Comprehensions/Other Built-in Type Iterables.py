#Other Built-in Type Iterables
d1={'a':1,'b':2,'c':3}
for keys in d1:
    print(keys,d1[keys])
i=iter(d1)
k=next(i)
print(k,d1[k])
k=next(i)
print(k,d1[k])
r1=range(5)
i2=iter(r1)
print(next(i2))
print(next(i2))
print(next(i2))
print(next(i2))
print(next(i2))
l1=[1,2,3]
e=enumerate(l1)
i3=iter(e)
print(next(i3))
