#list
l1=[]
print('An empty list',l1)
l2= [123, 'abc', 1.23, {'raju','mane',12,12.34}]
print('Four items: indexes 0..3',l2)
l3=  ['Bob', 40.0, ['dev', 'mgr']]
print('Nested sublists',l3)
l4=  list('123')
print('List of an iterable’s items',l4)
l4=  list('raju')
print('List of an iterable’s items',l4)
l5=  list(range(-4, 4))
l6=[1]
print('list of successive integers',l5)
print('Index',l2[2])
print('index of index',l3[2][0])
print('slice',l2[1:3])
print('length',len(l3[2]))
print('Concatenate',l2+l3)
print('repeat',l6*10)
print('Iteration')
for i in l2:
    print(i)
print('membership','abc' in l2)
print('Methods: growing')
print('append',l1.append(1),l1)
print('append',l1.append([2,3]),l1)
print('extend',l1.extend([2,3]),l1)
print('extend',l1.extend([2,3,['raju']]),l1)
print('insert',l1.insert(6,4),l1)
print('Methods: searching')
print('index',l1.index([2,3]),l1)
print('count',l1.count(2),l1)
print('Methods: sorting, reversing,')
l7=[0,4,6,8,10,1,3,2,5]
print('sort',l7.sort(),l7)
print('reverse',l7.reverse(),l7)
print('copying (3.3+), clearing (3.3+)')
l8=l7.copy()
print('copy',l8,l7)
print('clearing',l8.clear(),l8)
print('Methods, statements: shrinking')
print('pop',l7.pop(5),l7)
print('remove',l7.remove(5),l7)
del l7[5]
print('del',l7)
del l7[1:3]
print('del',l7)
l7[1:3]=[]
print('del',l7)
print('Index assignment, slice assignment')
l7[1]=1
print('Index assignment',l7)
l7[:]=[1,['raju']]
print('Index assignment',l7)
