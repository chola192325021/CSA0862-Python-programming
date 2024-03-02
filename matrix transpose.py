a=[[1,1,1],[2,2,2],[3,3,3]]
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        b[i][j]=a[j][i]
for i in b:
    print(i)
