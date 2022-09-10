#global 
x=10
def test():
    global x
    x=11
    print('in def',x)

test()
print('in module',x)
