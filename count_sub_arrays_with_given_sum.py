arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
l,r=0,0
currsum=0
count=0
for r in range(n):
    currsum+=arr[r]
    if currsum==k:
        count+=1
    elif currsum>k:
        currsum-=arr[l]
        l=l+1
        if currsum==k:
            count+=1
print(count)
