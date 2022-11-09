#Functional Programming Tools
p=print
counter=[1,2,3,4]
t=1,2,3,4
def inc(x):
    return x+10

update=list(map(inc,counter))
p(update,counter)
t1=list(map(inc,t))
p(t1,t)
l=list(map((lambda x:x+10),counter))
p(l,counter)

#filter
l2=list(range(-5,5))
p(l2)
l3=list(filter((lambda x:x if not x%2==0 else 0),range(-100,100)))
p(l3)

#reduce
from functools import reduce
r1=reduce((lambda x,y:x+y),[1,2,3,4])
p(r1)
r1=reduce((lambda x,y:x*y),[1,2,3,4])
p(r1)

import operator, functools
f1= functools.reduce(operator.add, [2, 4, 6])
p(f1)
