#thismod
var=99
#print('module var',var)
def local():
    var=0
    #print('var in local',var)
#local()
#print('module var after local',var)
print()
def global1():
    global var
    var +=1
    #print('var in global1',var)
#global1()
#print('module var after global1',var)
print()
def global2():
    var=0
    import thismod
    thismod.var +=1
    #print('var in global2 after importing thismod',thismod.var)
#global2()
#print('module var after global2',var)
#print('#######################')
def global3():
    var=0
    import sys
    glob=sys.modules['thismod']
    glob.var +=1
    #print('var in global3 after importing sys',glob.var)
#global3()
#print('module var after global3',var)
def test():
    print(var)
    local()
    global1()
    global2()
    global3()
    print(var)

