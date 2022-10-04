#Arbitrary Arguments Examples
#packing
def f(*name):
    print(name)

f(1,2,3)
f(1,2,{'name':'raju'},[1,2,3])


def f1(a, *pargs, **kargs):
    print(a, pargs, kargs)

f1(1, 2, 3,x=1, y=2)

#unpacking
def f2(a,b,c,d):
    print(a,b,c,d)

args=1,2,3,4
f2(*args)
args={'a': 1, 'b': 2, 'c': 3,'d':4}
f2(**args)
f2(1,*(2, 3), **{'d': 4})
f2(1, c=3, *(2,), **{'d': 4})
f2(1, *(2, 3), d=4)
f2(1, *(2,), **{'d':4},c=3)
