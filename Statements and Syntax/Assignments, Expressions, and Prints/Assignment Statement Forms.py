#Assignment Statement Forms
spam = 'Spam'
print('Basic form',spam)
spam, ham = 'yum', 'YUM'
print('Tuple assignment (positional)',(spam,ham))
[spam, ham] = ['yum', 'YUM']
print('List assignment (positional)',[spam,ham])
a,b,c,d='spam'
print('Sequence assignment, generalized',[a,b,c,d])
a, *c,b = 'spam'
print('Extended sequence unpacking (Python 3.X)',(a,c,b))
spam = ham = 'lunch'
print('Multiple-target assignment',spam,ham)
a=10
a += 42
print('Augmented assignment',a)

