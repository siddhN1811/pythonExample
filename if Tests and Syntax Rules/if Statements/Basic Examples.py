#Basic Examples
if 0:
    print('true')
print('false')

a=10
b=20
if a<b:
    print('a<b')
else:
    print('a>b')
a1,a2,a3,a4,a5=40,50,60,70,80
marks,avg=(a1+a2+a3+a4+a5),(a1+a2+a3+a4+a5)/5
print(marks,avg)
if avg>=85.00:
    print('A')
elif avg>=70 and avg<85:
    print('B')
elif avg>=55 and avg<70:
    print('C')
elif avg>=35 and avg<55:
    print('D')
else:
    print('F')

print()
choice = 'ham'   
d1={'spam': 1.25, 'ham': 1.99,'eggs': 0.99,'bacon': 1.10}
print(d1[choice])
print(d1.get('spam',"it's not you"))
print(d1.get('bcon',"it's not you"))

if choice in d1:
    print(d1[choice])
else:
    print("it's not you")
