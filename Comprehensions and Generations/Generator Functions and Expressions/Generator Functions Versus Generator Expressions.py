#Generator Functions Versus Generator Expressions
p=print
g1=(c*4 for c in 'spam')
p(next(g1))
p(next(g1))
p(next(g1))
p(next(g1))
p()
def timesfour(s):
    for c in s:
        yield c*4

f1=timesfour('spam')
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
