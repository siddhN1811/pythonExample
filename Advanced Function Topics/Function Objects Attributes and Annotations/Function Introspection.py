#Function Introspection
def func(a):
    b='spam'
    return b*a

print(func(8))
print(func.__name__)
print(dir(func))
func.count=1
print(dir(func))
print()
print(dir(func.count))
func.test="pass"
print(dir(func))
