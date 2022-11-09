#Example: List Comprehensions and Matrixes
p=print
m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
n=[
    [2,2,2],
    [3,3,3],
    [4,4,4]
    ]
p(m)
p(n)
p(m[1])
p(m[1][2])
res1=[row[1] for row in m]
p(res1)
res2=[m[row][1] for row in range(3)]
p(res2)
res3=[x for x in m]
p(res3)
res4=[m[i][i] for i in range(3)]
p(res4)
res5=[m[i][len(m)-1-i] for i in range(len(m))]
p(res5)
res6=[[m[i][j]+10  for j in range(len(m))] for i in range(len(m))]
p(res6)
res6=[j+10 for i in m for j in i]
p(res6)
res7=[[col + 10 for col in row] for row in m]
p(res7)
res8=[m[r][c]*n[r][c] for r in range(len(m)) for c in range(len(n))]
p(res8)
res9=[[m[r][c]*n[r][c] for c in range(len(n))] for r in range(len(m))]
p(res9)
