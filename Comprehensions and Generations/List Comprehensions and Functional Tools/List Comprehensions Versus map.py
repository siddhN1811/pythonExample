#List Comprehensions Versus map
p=print
o1=ord('r')
p(o1)
p()
res1=[]
for x in 'spam':
    res1.append(ord(x))
p(res1)
res2=list(map(ord,'spam'))
p(res2)
res3=[ord(x) for x in 'spam']
p(res3)
res4=[x**2 for x in range(10)]
p(res4)
res5=list(map((lambda x:x**2),range(10)))
p(res5)
