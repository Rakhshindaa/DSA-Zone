n,m=map(int,input().split())
ans=[]
for i in range(n):
    a=list(map(int,input().split()))
    ans.append(sum(a))
for i in ans:
    print(i)