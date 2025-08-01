arr=list(map(int,input().split()))
n=len(arr)
l=0
r=n-1
while l<=r:
    mid=(l+r)//2
    if mid==n-1 or arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
        print(arr[mid])
        break
    elif mid%2==0 and arr[mid]==arr[mid+1]:
        l=mid+1
    elif mid%2==0 and arr[mid]==arr[mid-1]:
        r=mid-1
    elif mid%2!=0 and arr[mid]==arr[mid+1]:
        r=mid-1
    elif mid%2!=0 and arr[mid]==arr[mid-1]:
        l=mid+1