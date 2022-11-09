#Comprehension Syntax Summary
p=print
l1= [x * x for x in range(10)]
p(l1)
p()
g1=(x * x for x in range(10))
p(next(g1))
p(next(g1))
p()
s1={x * x for x in range(10)}
p(s1)
p()
s2={1,2,3}
g1=iter(s2)
p(next(g1))
p()
p(s2)
for i in s2:
    print(i)

p()
d1={x: x * x for x in range(10)}
p(d1)
