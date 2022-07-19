#Indexing and Slicing
print('Indexing')
s1='siddhanth ganesh naidu'
print('name: ',s1,len(s1))
print('positive index s1[8]: ',s1[8])
print('negative index s1[-14]: ',s1[-14])
print()
print('Slicing')
print('general Slicing: ',s1[:])
print('postive Slicing: ',s1[0:])
print('postive Slicing: ',s1[:len(s1)])
print('postive Slicing: ',s1[4:12])
print('negative Slicing:',s1[-22:])
print('negative Slicing: ',s1[-21:-7])
print('The third limit Slicing: ',s1[::2])
print('The third limit Slicing: ',s1[2:12:2])
s2='hello'
print('The third limit Slicing: ',s2[1:3:-2])
