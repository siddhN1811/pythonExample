#Dictionaries
'''d1={}
print('Empty dictionary',d1)
d2={'name': 'Bob', 'age': 40}
print('Two-item dictionary',d2)
d3={'cto': {'name': 'Bob', 'age': 40,'skill':['java','python']}}
print('Nesting',d3)
d4= dict(name='Bob', age=40)
print('Alternative construction techniques:',d4)
d5= dict([('name', 'Bob'), ('age', 40)])
print('keywords:',d5)
'''
l1 = list(input(''))
for i in l1 range(0,len(l1)-1):
    for j in l1 range(i+1,len(l1)-1):
        if l1[i]==l1[j]:
            print("true")
            break
            
