#Storing Python Objects in Files: Conversions
X, Y, Z = 43, 44, 45
S ='Spam'
D ={'a': 1, 'b': 2}
L =[1, 2, 3]
f1=open('Storing Python Objects in Files.txt', 'w')
f1.write(S + '\n') # Terminate lines with \n
f1.write('%s,%s,%s\n' % (X, Y, Z)) # Convert numbers to strings
f1.write(str(L) + '$' + str(D) + '\n')
f1.close()
read= open('Storing Python Objects in Files.txt').read()
print(read)
f2=open('Storing Python Objects in Files.txt')
line1=f2.readline()
print(line1)
line2=f2.readline()
print(line2)
parts=line2.split(',')
print(line2.split(','))
parts[-1]=parts[-1].rstrip()
print(parts)
print(parts[-1])
print( int(parts[1]))
number=[int(p) for p in parts]
print(number)
line3=f2.readline()
print(line3)
parts = line3.split('$')
print(parts)
l1= eval(parts[0])
print(l1[-1])
objects=[eval(p) for p in parts ]
print(objects)






