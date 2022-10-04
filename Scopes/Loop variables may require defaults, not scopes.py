#Loop variables may require defaults, not scopes
def makeactions():
    acts=[]
    for i in range(5):
        acts.append(lambda x,i=i:i**x)
    return acts
a=makeactions()
print(a[4](2))
