arr=list(map(int,input().split()))
k=int(input("window size:"))
n=len(arr)
ans=[]
d={}
for i in range(k):
    if arr[i] in d:
        d[arr[i]]+=1
    else:
        d[arr[i]]=1
ans.append(len(d))
for i in range(k,n):
    if arr[i] in d:
        d[arr[i]]+=1
    else:
        d[arr[i]]=1
    if d[arr[i-k]]==1:
        d.pop(arr[i-k])
    else:
        d[arr[i-k]]-=1
    ans.append(len(d))
print(ans)