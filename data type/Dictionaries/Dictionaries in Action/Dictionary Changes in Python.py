#Dictionary Changes in Python
l1=['a', 'b', 'c']
l2=[1, 2, 3]
l3=list(zip(l1,l2))
print('list zip',l3)
d1=dict(zip(l1,l2))
print('list dict',d1)
d2= {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print('d2',d2)
d3={x: x ** 2 for x in range(1,5)}
print('d3',d3)
d4= {c: c * 4 for c in 'SPAM'}
print('d4',d4)
d5= {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print('d5',d5)
d6={w:'www.'+w+'.in' for w in ['today','map']}
print(d6)
d7= dict.fromkeys(['a', 'b', 'c'], 0)
print(d7)
d8= {k:0 for k in ['a', 'b', 'c']}
print(d8)
d9= dict.fromkeys('spam')
print(d9)
d10= {k: None for k in 'spam'}
print(d10)
