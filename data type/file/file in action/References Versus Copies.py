#References Versus Copies
#pro
X = [1, 2, 3]
print(X)
L = ['a', X.copy(), 'b']
print(L)
D = {'x':X.copy(), 'y':2}
print(D)
X[1]='raju'
print(X)
print(L)
print(D)
x={'name':{'sname':{'0':'r','1':'a'},'lname':'mane'},'age':32,'salary':40000}
print(x)
y=x.copy()
print(y)

