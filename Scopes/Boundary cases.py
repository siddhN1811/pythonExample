#Boundary cases
'''def f1():
    def f2():
        counter=0
        def f3():
            nonlocal counter
            counter +=1
            print(counter)
        return f3
    b=f2()
    b()
    
f1()
'''
'''def f1(start):
    state=start
    def f2(label):
        nonlocal state
        print(label,state)
        state +=1
    return f2
f=f1(0)
f('spam')
f('raju')
g=f1(44)
g('rajesh')
g('suraj')
'''
def f1(start):
    global state
    state=start
    def f2(label):
        global state
        print(label,state)
        state +=1
    return f2
"""
f=f1(0)
f('spam')
f('raju')
g=f1(44)
g('rajesh')
g('suraj')
f('ram')
print(f1(0).state)        
"""
def f1(start):
    def f2(label):
        print(label,f2.state)
        f2.state +=1
    f2.state=start
    return f2

f=f1(0)
f('spam')
f('pam')
print(f.state,f.state)

