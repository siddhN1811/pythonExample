#Generator expressions
p=print
s='spam'
g1=(s[i:]+s[:i] for i in range(len(s)))
p(next(g1))
p(next(g1))
p(next(g1))
p(next(g1))
p()
f=lambda seq:(seq[i:]+seq[:i] for i in range(len(seq)))
p(list(f(s)))
p(list(f([1,2,3])))
for x in f((1,2,3)):
    print(x,end=' ')
