#Print Stream Redirection
import sys
a=10
b=20
c=a+b
sys.stdout.write('hello world')
sys.stdout.write(str(c))

temp=sys.stdout
sys.stdout=open('log.txt','a')
print('hello world')
print(1,2,3)
sys.stdout.close()
sys.stdout=temp
print('terminal')
print(open('log.txt').read())
d1={'name':'raju mane'}
l1=[1,2,3,4]
log=open('log.txt','a')
print(d1,file=log)
print(l1,file=log)
log.close()
sys.stderr.write(('Bad!' * 8) + '\n')


