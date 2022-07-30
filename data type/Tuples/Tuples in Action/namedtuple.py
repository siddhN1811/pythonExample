#namedtuple
from collections import namedtuple
std = namedtuple('std', ['name', 'age', 'jobs'])
std1=std(name='raju',age=32,jobs=['dev','mgr'])
print('std1',std1)
std2=std(name='ramesh',age=32,jobs=['dev'])
print('std2',std2)
#Converting to a dictionary supports key-based behavior when needed:
d1=std1._asdict()
print('d1',d1)
