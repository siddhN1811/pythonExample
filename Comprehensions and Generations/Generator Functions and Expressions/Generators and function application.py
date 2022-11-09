#Generators and function application
for x in 'spam':
    print(x.upper(),end=' ')
print()
l1=list(x.upper() for x in 'spam')
print(l1)
l2=list(x.upper() for x in 'spam')
print(l2)
print(*(x.upper() for x in 'spam'))
