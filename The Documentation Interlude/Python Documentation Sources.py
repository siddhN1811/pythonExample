import sys
print('sys: ',dir(sys))
print('len:',len(dir(sys)))
print('Non __X names only', len([x for x in dir(sys) if not x.startswith('__')]))
print('Non underscore names',len([x for x in dir(sys) if not x[0] == '_']))
print('list',dir([]))
print()
print('dict',dir({}))
print()
print('string',dir(''))
print()
print('tuple',dir(()))
a1=dir([])
print('a1',a1)
for i in a1:
    print(i)
print(len(dir([])), len([x for x in dir([]) if not x.startswith('__')]))
print(len(dir('')), len([x for x in dir('') if not x.startswith('__')]))
l1= [a for a in dir(list) if not a.startswith('__')]
print(l1)
l2=[a for a in dir(dict) if not a.startswith('__')]
print(l2)
