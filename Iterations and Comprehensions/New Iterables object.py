#Iterables
M = map(abs, (-1, 0, 1))
print(next(M))
print(next(M))
print(next(M))
for x in M:
    print(x)
print()
M2=map(abs, (-1, 0, 1))
for x in M2:
    print(x)
