#Comprehending Set and Dictionary Comprehensions
p=print
s1={x * x for x in range(10)}
p(s1)
s2= set(x * x for x in range(10))
p(s2)
d1={x: x * x for x in range(10)}
p(d1)
d2= dict((x, x * x) for x in range(10))
p(d2)
