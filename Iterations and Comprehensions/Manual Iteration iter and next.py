#Manual Iteration: iter and next
l1=[1,2,3]
i1=iter(l1)
print(i1.__next__())
print(i1.__next__())
print(i1.__next__())
l2=[1,2,3]
for x in l2:
    print(x**2,end=' ')
