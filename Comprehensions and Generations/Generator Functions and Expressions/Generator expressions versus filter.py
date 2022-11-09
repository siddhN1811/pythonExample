#Generator expressions versus filter
p=print
line='aa bbb c'
f1=filter((lambda x:len(x)>1),line.split())
p(type(f1))
p(next(f1))
p(next(f1))
g1=(x for x in line.split() if len(x)>1)
p(type(g1))
p(next(g1))
p(next(g1))
