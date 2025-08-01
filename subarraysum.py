arr=list(map(int,input().split()))
n=len(arr)
pre=[[arr[0]]]
minlen=0
for i in range(n):
    for j in range(i+1,n+1):
        if pre[j]-pre[i]>=target:
            minlen=min(minlen,j-1)
print(minlen)