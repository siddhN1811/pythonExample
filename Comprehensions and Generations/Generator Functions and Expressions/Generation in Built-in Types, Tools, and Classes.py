#Generation in Built-in Types, Tools, and Classes
p=print
d1={'a':1,'b':2,'c':3}
x=iter(d1)
p(next(x))
p(next(x))
p(next(x))
#Generators and library tools: Directory walkers
import os
for (root,sub,files) in os.walk(r'E:\python\pythonExamples\Comprehensions and Generations\Generator Functions and Expressions\code'):
    for name in files:
        if name.startswith('call'):
            p(root,':',name)
p()
g1=os.walk(r'E:\python\pythonExamples\Comprehensions and Generations\Generator Functions and Expressions\code')
p(next(g1))
p(next(g1))
p(next(g1))
p(next(g1))
