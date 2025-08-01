arr=list(map(int,input().split()))
n=len(arr)
dp=[1]*n
for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)
print('longest increasing subsequence length:',max(dp))