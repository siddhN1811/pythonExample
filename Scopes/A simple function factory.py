#A simple function factory
'''def maker(n):
    def action(x):
        return x**n
    return action
f=maker(2)
print(f(3))
g=maker(3)
print(f(3),g(3))'''
#lambda
'''def f1(n):
    return lambda x:x**n
h=f1(2)
print(h(3))'''
action=lambda x:x**2
print(type(action))
