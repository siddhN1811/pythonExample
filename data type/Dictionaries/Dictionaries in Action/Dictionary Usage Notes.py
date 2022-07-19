#Dictionary Usage Notes
l1=[1,2,3]
print('l1',l1)
d1={}
d1[99] = 'spam'
print('d1',d1)
Matrix = {}
print('Matrix',Matrix)
Matrix[(2, 3, 4)] = 88
print('Matrix',Matrix)
Matrix[(7, 8, 9)] = 99
print('Matrix',Matrix)
if (2,2,2) in Matrix:
    print(Matrix[(2,2,2)])
else:
    print('0')
try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)
print( Matrix.get((2, 3, 4), 0))
print( Matrix.get((2, 3, 6), 0))
rec = {'name': 'Bob', 'jobs': ['developer', 'manager'],'web': 'www.bobs.org/˜Bob', 'home': {'state': 'Overworked', 'zip': 12345}}
print('rec',rec)
print('rec',rec['name'])
print('rec',rec['home']['zip'])
l2=[]
l2.append(rec)
d2={'name': 'Raju Mane', 'jobs': ['developer', 'programmer'],'web': 'www.bobs.org/˜Bob', 'home': {'state': 'MH', 'zip': 400018}}
l2.append(d2)
print('l2',l2)
for i in l2:
    print(i)

print("l2[0]['jobs']",l2[1]['home']['state'])
l3=['0','1','2','3']
d3={}
for i in l3:
    d3[i]=0
print()
print(d3)

