'''
1] Given two integer numbers return their product only if the product is
equal to or lower than 1000,
else return their sum.'''
'''
n1 = int(input('Enter No. 1: '))
n2 = int(input('Enter No. 2: '))
mul = n1*n2
if(mul<=1000):
    print('Mul: ',mul)
else:
    print('sum: ',n1+n2)

-----------------------------------------------------------------------------'''

'''
2] Write a program to iterate the first 10 numbers and in each iteration,
print the sum of the current and previous number.'''
'''
for i in range(0,9):
    sum = i+(i-1)
    if(sum>=0):
        print('current Number %d, previous number %d'%(i,i-1))
        print('sum:',sum)
------------------------------------------------------------------------------'''


'''
3] Write a program to accept a string from the user and display characters that are
present at an even index number.'''
'''
str = input('Enter a String')
for i in str:
    if i%2==0:
        print(i)'''
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()









