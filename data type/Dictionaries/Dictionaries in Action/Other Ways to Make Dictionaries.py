#Other Ways to Make Dictionaries
s1='Bob'
s2=40
d1=dict(name=s1, age=s2)
print('dict keyword argument form',d1)
s1=('name', 'Bob')
s2=('age', 40)
l1=[s1, s2]
d2=dict(l1)
print('dict key/value tuples form',d2)
d3= dict.fromkeys(['name', 'age'], 0)
print('formkeys',d3)
d3['name']='Bob'
d3['age']=40
print('formkeys',d3)
l2=[1,1,3]
print(l2)
d4={'name':'raju','name':'ramesh'}
print(d4)
