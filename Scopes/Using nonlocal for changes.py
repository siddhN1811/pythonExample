#Using nonlocal for changes
def t(start):
    state=start
    def n(label):
        nonlocal state
        print(label,state)
        state +=1
    return n
f=t(0)
f('spam')
f('raju')
