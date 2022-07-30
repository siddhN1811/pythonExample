#Storing Native Python Objects: pickle
d1= {'a': 1, 'b': 2}
f1= open('Storing Native Python Objects pickle.pkl', 'wb')
import pickle
pickle.dump(d1, f1)
f1.close()
f2 = open('Storing Native Python Objects pickle.pkl', 'rb')
d2= pickle.load(f2)
print(d2)
print( open('Storing Native Python Objects pickle.pkl', 'rb').read())
