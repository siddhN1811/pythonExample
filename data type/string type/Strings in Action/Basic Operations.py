#Basic Operations
s1='raju '
s2='mane'
print('fname',s1,len(s1))
print('lname',s2,len(s2))
print('concate',s1+" "+s2)
print('Repetition:',s1*4)
print('-' * 80)
s3='hacker'
for i in s3:
    print(i,end=' ')
    
print('\nFound','ke'in s3)
print('Not Found','z' in s3)
s4 = 'abcspamdef'
print('Substring search','spam'in s4)
