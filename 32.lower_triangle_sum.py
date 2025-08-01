n=int(input())
m=[]
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
tsum=0
for i in range(n):
    for j in range(i+1):
        tsum+=m[i][j]
print(tsum)