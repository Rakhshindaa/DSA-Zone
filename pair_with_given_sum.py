arr=list(map(int,input().split()))
target=int(input())
d={}
for i in range(len(arr)):
    d[arr[i]]=i
for i in arr:
    if target-i in arr:
        print([d[i],d[target-i]])
        break