#Generalized Set Functions
def intersection(*args):
    res=[]
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res
    #print(args[0],args[1])

s1,s2='spam','scam'
intersection(s1,s2)
