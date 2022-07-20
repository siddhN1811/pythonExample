#Tuple syntax peculiarities: Commas and parentheses
t1= 1, 2, + 3, 4,
print('Concatenation',t1)
t2= (1, 2) * 4
print('Repetition',t2)
t3=t1[0]
print('indexing',t3)
t4=t1[1:3]
print('slicing',t4)
t5=len(t1)
print('length',t5)
