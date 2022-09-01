#Changing Lists: range Versus Comprehensions
l1=[1,2,3,4,5]
for i in l1:
    i +=1
print(l1,i)

for j in range(len(l1)):
    l1[j] +=1

print(l1)

l2=[x+1 for x in l1]
print(l2)
