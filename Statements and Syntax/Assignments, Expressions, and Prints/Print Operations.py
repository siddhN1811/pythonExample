#Print Operations #The 3.X print function in action
print()
x,y,z,w='spam',99,['eggs'],{'name':'raju'}
print(x,y,z,w,sep=' ')
print(x,y,z,w,end='')
print(x,y,z,w)
print(x,y,z,w,end='...\n')
print(x,y,z,w,end='...\n')
print(x,y,z,w,sep='...',end='!\n')
print(x, y, z,w,sep='...', file=open('data.txt', 'w'))
print(open('data.txt').read())
text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)
print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))
    
