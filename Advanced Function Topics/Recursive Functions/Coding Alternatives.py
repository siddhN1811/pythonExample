#Coding Alternatives
def mysum1(l):
    return l[0] if len(l)==1 else l[0]+mysum1(l[1:])

print(mysum1([1,2,3,4,5]))

def mysum2(l):
    first,*rest=l
    print(first,rest)
    return first if not rest else first+mysum2(rest)

print(mysum2([1,2,3,4,5]))

def mysum(l):
    if not l:
        return 0
    return nonempty(l)

def nonempty(l):
    return l[0]+mysum(l[1:])

print(mysum([1.1, 2.2, 3.3, 4.4]))
