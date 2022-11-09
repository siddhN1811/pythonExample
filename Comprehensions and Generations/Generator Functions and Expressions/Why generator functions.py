#Why generator functions?
p=print
def ups(line):
    for sub in line.split(','):
        yield sub.upper()

a=ups('aaa,bbb,ccc')
p(next(a))
p(next(a))
p(next(a))
t=tuple(ups('aaa,bbb,ccc'))
p(t)
e={i:s for (i,s) in enumerate(ups('aaa,bbb,ccc'))}
p(next(e))
