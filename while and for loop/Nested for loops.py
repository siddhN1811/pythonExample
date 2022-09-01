#Nested for loops
items = ["aaa", 111, (4, 5), 2.01] 
tests = [(4, 5), 3.14]
for keys in tests:
    for item in items:
        if keys==item:
            print(keys,'was found')
            break
    else:
        print(keys,'not found')
seq1='spam'
seq2='scam'
res=[]
for x in seq1:
    if x in seq2:
        res.append(x)

print(res)
l1=[x for x in seq1 if x in seq2]
print(l1)
