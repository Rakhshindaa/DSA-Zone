n=int(input())
arr=list(map(str,input().split()))
arr.sort()
i=1
f=arr[0]
s=arr[:-1]
while f[i]==s[i]:
    i=i+1
print(f[:i+1])
