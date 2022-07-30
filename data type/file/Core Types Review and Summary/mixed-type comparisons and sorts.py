# mixed-type comparisons and sorts
print(" 11 == '11'",11 == '11')
#print(" 11 >= '11'",11 >= '11') TypeError: '>=' not supported between instances of 'int' and 'str'
l1=['11','12','10','9','91','13','87']
l1.sort()
print(l1)
l2=['raju','ramesh','rajendra','rajani']
l2.sort()
print(l2)
l3=[9,8,7,6,5,4,3,2,1]
l3.sort()
print(l3)
l4=[int('11'),12]
l4.sort()
print(l4)

