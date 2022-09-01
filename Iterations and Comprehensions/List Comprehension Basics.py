#List Comprehension Basics
f = open('script2.py')
lines = f.readlines()
print(lines)
lines = [line.rstrip() for line in lines]
print(lines)
l2=list(range(10))
l3=[x for x in l2 if x%2==0]
print(l3)
print()
l4=[x*y for x in range(1,10) for y in range(1,10)]
print(l4)
L = [11, 22, 33, 44]
L[1:3] = open('script2.py')
print(L)
l2=list(open('script2.py'))
print(l2)
a=any(['spam','','ni'])
print(a)
a=all(['spam','','ni'])
print(a)

