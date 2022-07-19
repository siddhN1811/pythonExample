#Dictionaries
d1={}
print('Empty dictionary',d1)
d2={'name': 'Bob', 'age': 40}
print('Two-item dictionary',d2)
d3={'cto': {'name': 'Bob', 'age': 40,'skill':['java','python']}}
print('Nesting',d3)
d4= dict(name='Bob', age=40)
print('Alternative construction techniques:',d4)
d5= dict([('name', 'Bob'), ('age', 40)])
print('keywords:',d5)
