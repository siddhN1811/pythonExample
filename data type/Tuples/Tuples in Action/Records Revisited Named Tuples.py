#Records Revisited: Named Tuples
t1 = ('Bob', 40.5, ['dev', 'mgr'])
print('bob',t1)
print('bob[0]',t1[0])
print('bob[1]',t1[1])
print('bob[2]',t1[2][0])
print()
d1= dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print('d1',d1)
print('d1',d1['name'])
print('d1',d1['jobs'][0])
print('tuple',tuple(d1.keys()))
print('tuple',tuple(d1.values()))
from collections import namedtuple
std = namedtuple('std', ['name', 'age', 'jobs'])
print('std',std)
raju=std(name='raju',age=32,jobs=['dev','mgr'])
print('raju',raju.jobs[0])
ramesh=std(name='ramesh',age=22,jobs=['dev'])
print('ramesh',ramesh)
d2=raju._asdict()
print('d2',d2)
