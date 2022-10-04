#The min Wakeup Call!
'''
def min3(*args):
    #print(args)
    tmp = list(args) # Or, in Python 2.4+: return sorted(args)[0]
    print(tmp)
    tmp.sort()
    return tmp[0]

print(min3([1,2,0], [1,3], [1,2,1]))

#min3([2,2], [1,1], [3,3])
'''
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res
def lessthan(x, y): return x < y # See also: lambda, eval
def grtrthan(x, y): return x > y
print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # Self-test code
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
