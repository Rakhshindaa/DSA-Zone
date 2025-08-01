arr=list(map(int,input().split()))
n=len(arr)
dp=arr.copy()
for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+arr[i])
print('Maximum sum of increasing subsequence length:',max(dp))