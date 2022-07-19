# decimal
from decimal import Decimal
x='0.1'
y='0.2'
z='0.3'
a1=Decimal(x)
a2=Decimal(y)
a3=Decimal(z)
print('decimal a1:',a1,' a2:',a2)
print('add',a1+a2)
print('sub',a1-a2)
print('mul',a1*a2)
print('div',a1/a2)
print('mod',a1%a2)
print('less than',a1<a2)
print('less than or equal to',a1<=a2)
print('greater than',a1>a2)
print('greater than or equal to',a1>=a2)
print('equal to',a1==a2)
print('not equal to',a1!=a2)
print('and',a1<a2 and a1!=a2)
print('chained',a1<a2<a3)
#print('decimal a3',a3)
