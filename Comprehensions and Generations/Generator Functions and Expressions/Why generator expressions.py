#Why generator expressions?
p=print
m1=map(abs, (-1, -2, 3, 4))
p(type(m1))
p(next(m1))
p(next(m1))
g1=(abs(x) for x in (-1,2,3,4))
p(type(g1))
p(next(g1))
p(next(g1))
# Nested comprehensions
l1=[x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]
p(l1)
m2=[map(lambda x: x * 2, map(abs, (-1, -2, 3, 4))),map(lambda x: x * 3, map(abs, (-1, -2, 3, 4)))]
p(next(m2[0]))
p(next(m2[0]))
p(next(m2[1]))
print()
g2=[(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))),(x * 3 for x in (abs(x) for x in (-1, -2, 3, 4)))]
p(next(g2[0]))
p(next(g2[1]))

