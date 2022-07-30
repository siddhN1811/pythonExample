#Storing Python Objects in JSON Format
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)
import json
s1 = json.dumps(rec)
print(s1)
s2=json.loads(s1)
print(s2)
f1=json.dump(rec, fp=open('testjson.json', 'w'), indent=2)
print(open('testjson.txt').read())
f2= json.load(open('testjson.txt'))
print(f2)


