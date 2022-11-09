#Generator Expressions: Iterables Meet Comprehensions
p=print
l1=[x**2 for x in range(10)]
p(l1)
g1=(x**2 for x in range(3))
p(type(g1))
p(next(g1))
p(next(g1))
p(next(g1))
g2=(x.upper() for x in 'aaa,bbb,ccc'.split(','))
z=''.join(g2)
p(z)
a,*b=(x.upper() for x in 'aaa,bbb,ccc'.split(','))
p(a,b)
s1=sum(x ** 2 for x in range(4))
p(s1)
s2=sorted(x ** 2 for x in range(4))
p(s2)
s3=sorted((x ** 2 for x in range(4)), reverse=True)
p(s3)

