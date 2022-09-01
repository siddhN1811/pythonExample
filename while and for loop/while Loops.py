#while Loops
x='raju'
while x:
    print(x,end=' ')
    x=x[:-1]

print('0 to 9 number')
a,b=0,10
while a<b:
    print(a,end=' ')
    a +=1
'''
a=1
while a:
    pass
'''
print('continue')
x=10
while x:
    x -=1
    if x % 2 != 0:
        continue
    print(x,end=' ')
'''
while True:
    name=input('enter name:')
    if name=='stop':
        break
    age=input('enter age')
    print(name,age)
'''
print()
y=10
x=y//2
while x>1:
    if y % x ==0:
        print(y,'has a factor of ',x)
        break
    x -=1
else:
    print(y,'is prime number')
