import time
def timer(func, *args): # Simplistic timing function
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start