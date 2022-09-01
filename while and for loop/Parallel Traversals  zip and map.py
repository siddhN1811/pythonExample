#Parallel Traversals: zip and map
l1=[1,2,3,7,5]
l2=[1,2,3,4,5]
for (x,y) in zip(l1,l2):
    print(x,y,' ',x+y)
    
