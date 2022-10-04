#Function Annotations
p=print
def func(a:'spam',b:(1,10),c:float) -> int:
    return a+b+c

p(func(1,2,3.5))
