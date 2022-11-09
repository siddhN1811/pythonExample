#Generator functions in action
p=print
def gensquare(n):
    for i in range(n):
        yield i**2
x=gensquare(5)
y=gensquare(5)
p(x.__next__(),next(y))
p(x.__next__(),next(y))
p(x.__next__(),next(y))
p(x.__next__(),next(y))
p(x.__next__(),next(y))
z=gensquare(5)
b=iter(z) is z
p(b)

