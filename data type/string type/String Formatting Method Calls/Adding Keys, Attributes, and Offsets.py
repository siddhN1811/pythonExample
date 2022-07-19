#Adding Keys, Attributes, and Offsets
import sys
s1= 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
print('s1',s1)
s2= 'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
print('s2',s2)
s3=list('python')
print(s3)
s4='first={0[0]}, third={0[2]}'.format(s3)
print("s3=list('python')",s4)
s5='first={0}, last={1}'.format(s3[0], s3[-1])
print("s3=list('python')",s5)
parts = s3[0], s3[-1], s3[1:3]
s6 ='first={0}, last={1}, middle={2}'.format(*parts)
print("s3=list('python')",s6)
