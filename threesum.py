arr=list(map(int,input().split()))
n=len(arr)
ans=set()
arr.sort()
n=len(arr)
for i in range(n-2):
    l=i+1
    r=n-1
    while l<r:
        s=arr[i]+arr[l]+arr[r]
        if s<0:
            l=l+1
        elif s>0:
            r=r-1
        else:
            ans.add((arr[i],arr[l],arr[r]))
            l=l+1
            r=r-1
            while l<r and arr[l]==arr[l-1]:
                l=l+1
            while l<r and arr[r]==arr[r+1]:
                r=r-1
print(list(ans))