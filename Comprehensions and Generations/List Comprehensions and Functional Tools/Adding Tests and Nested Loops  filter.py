#Adding Tests and Nested Loops: filter
p=print
res1=[x for x in range(10)]
p(res1)
res2=[x for x in range(10) if x%2==0]
p(res2)
res3=[x for x in range(10) if not x%2==0]
p(res3)
res4=list(filter((lambda x:x%2==0),range(10)))
p(res4)
res5=[x**2 for x in range(10) if x%2==0]
p(res5)
res6=list(map((lambda x:x**2),filter((lambda x:x%2==0),range(10))))
p(res6)

#Formal comprehension syntax
res7=[x+y+z for x in [0,1,2] for y in [10,20,30] for z in [100,200,300]]
p(res7)
res8=[x+y for x in 'spam' for y in 'SPAM']
p(res8)
res9=[x+y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P',"A")]
p(res9)
res10= [x + y + z for x in 'spam' if x in 'sm'
         for y in 'SPAM' if y in ('P', 'A')
         for z in '123' if z > '1']
p(res10)
res10=[(x,y) for x in range(5) if x%2==0 for y in range(5) if not y%2==0]
p(res10)
 
