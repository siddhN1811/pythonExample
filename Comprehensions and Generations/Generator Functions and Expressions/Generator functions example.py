#Generator functions
p=print
def sequence(seq):
    for i in range(len(seq)):
        seq=seq[1:]+seq[:1]
        yield seq
f1=sequence('ramchandra')
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p(next(f1))
p()
def sequence1(seq):
    for i in range(len(seq)):
        yield seq[i:]+seq[:i]
f2=sequence1('...\\\\...')
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
p(next(f2))
