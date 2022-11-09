import time
'''
def sum(l):
    c=0
    for i in l:
        c=c+i
    return c
d=sum([x for x in range(1000)])
end1=time.process_time()
print(d,end1)
e=sum([x for x in range(722)])
end2=time.process_time()
print(e,end2)
'''
def sum(l):
    c=0
    for i in l:
        c=c+i
    return c
d=sum([x for x in range(100)])
end1=time.perf_counter()
print(d,end1)
e=sum([x for x in range(722)])
end2=time.perf_counter()
print(e,end2)
