#Anonymous Functions: lambda
p=print
def func(x,y,z):
    return x+y+z

p(func(1,2,3))

f= lambda x,y,z:x+y+z
p(f(1,2,3))

x = (lambda a="fee", b="fie", c="foe": a + b + c)
p(x("wee"))

def name():
    title='sir'
    #action=lambda x:title +' '+x
    return lambda x:title +' '+x

act=name()
msg=act('spam')
p(msg)

l = [lambda x: x ** 2, lambda x: x ** 3,lambda x: x ** 4]
p(l[0](3))
for i in l:
    p(i(2))

d={'already': (lambda: 2 + 2),'got': (lambda: 2 * 4),'one': (lambda: 2 ** 6)}
p(d['got']())
