#second example
def intersect(seq1,seq2):
    res=[x for x in seq1 if x in seq2]
    return res

seq1=[1,2,4,5,6]
seq2=[4,5,6,8,9]
print(intersect(seq1,seq2))
seq1='spam'
seq2='spcm'
print(intersect(seq1,seq2))
seq1=(1,2,3)
seq2=(2,3)
print(intersect(seq1,seq2))
seq1={'name':'raju','age':30}
seq2={'name':'rajesh'}
print(intersect(seq1,seq2))
print(intersect([1, 2, 3], (1, 4)))
