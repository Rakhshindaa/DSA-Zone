#directions possible are left to right and top to bottom
m,n=map(int,input().split())
grid=[]
for _ in range(m):
    a=list(map(int,input().split()))
    grid.append(a)
dp=[[0]*n for _ in range(m)]
if grid[0][0]==1 or grid[m-1][n-1]==1:
    print('No path')
else:
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                if i>0:
                    dp[i][j]=dp[i-1][j]+dp[i][j]
                if j>0:
                    dp[i][j]=dp[i][j-1]+dp[i][j]
    print("number of unique paths =",dp[m-1][n-1])