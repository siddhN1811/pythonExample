#Nonexhaustive Traversals: range Versus Slices
s='abcdefghijk'
l1=list(range(0,len(s),2))
print(l1)
print()
for i in range(0,len(s),2):
    print(s[i],end=' ')
print()
for i in s[::2]:
    print(i,end=' ')

