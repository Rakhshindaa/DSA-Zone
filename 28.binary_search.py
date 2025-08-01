n,k=map(int,input().split())
arr=list(map(int,input().split()))
l=0
r=n-1
ans="False"
while l<=r:
    mid=(l+r)//2
    print(l,mid,r)
    if arr[mid]==k:
        ans="True"
        break
    elif arr[mid]>=arr[l]:
        l=mid+1
    else:
        r=mid-1
print(ans)