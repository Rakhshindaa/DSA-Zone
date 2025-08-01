n=int(input())
r1,c1,r2,c2=map(int,input().split())
m=[]
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
pre=[[0]*n for i in range(n)]
for r in range(n):
    for c in range(n):
        if r==0:
            pre[r][c]=pre[r][c-1]+m[r][c]
        elif c==0:
            pre[r][c]=pre[r-1][c]+m[r][c]
        elif r==0 and c==0:
            pre[r][c]=m[r][c]
        else:
            pre[r][c]=pre[r-1][c]+pre[r][c-1]+m[r][c]-pre[r-1][c-1]
curr=pre[r2][c2]
if c1!=0:
    left_cut=pre[r2][c1-1]
else:
    left_cut=0
if r1!=0:
    upper_cut=pre[r1-1][c2]
else:
    upper_cut=0
if r1!=0 and c1!=0:
    repeat=pre[r1-1][c1-1]
else:
    repeat=0
print(curr-left_cut-upper_cut+repeat)