#Arguments and Shared References
'''def f(a):
    a=99
    print('a',a)

b=88
f(b)
print(b)
'''
def changer(a,b):
    b=b[:]
    a=1
    b[0]='spam'
    print('in function',a,b)

x=0
l=[1,2]
changer(x,l)
print('outside function',x,l)
