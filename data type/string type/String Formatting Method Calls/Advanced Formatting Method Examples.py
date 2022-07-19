#Advanced Formatting Method Examples
import sys
s1= '{0:#>10} = {1:=+020,}'.format('spam', 128976543.4567)
print('s1',s1)
s2= '{0:10} = {1:10}'.format('spam', 123.4567)
print('s2',s2)
s3='{0:>10} = {1:<10}'.format('spam', 123.4567)
print('s3',s3)
s4='{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop'))
print('s4',s4)
s5='{0:e}, {1:.3e}, {2:.3g} {3:.4g} {4:f}'.format(3.14159, 3.14159,3.14159, 3.14159,3.1415967)
print('s5',s5)
s6='{0:f}, {1:.2f}, {2:>010.2f}'.format(3.14159, 3.14159, 3.14159)
print('s6',s6)

