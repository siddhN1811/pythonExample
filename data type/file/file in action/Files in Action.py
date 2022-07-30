#Files in Action
f1 = open('myfile.txt', 'w')
f1.write('hello text file.\n')
f1.write('goodbye text file\n')
f1.close()

f2= open('myfile.txt')
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(open('myfile.txt').read())
for line in open('myfile.txt'):
    print(line,end='')
a = open('myfile.txt').read()



    
