import time
p=print
def timer(func,*args):
    start=time.time()
    for i in range(1000):
        func(*args)
    return time.time()-start
p(timer(pow,2,100))
