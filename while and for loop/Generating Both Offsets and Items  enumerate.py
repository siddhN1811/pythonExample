#Generating Both Offsets and Items: enumerate
name='raju'
for (o,i) in enumerate(name):
    print(i,o)
E=enumerate(name)
print(next(E))
l2= [c * i for (i, c) in enumerate(name)]
print(l2)
