arr=list(map(int,input().split()))
m=int(input())
q=[]
for i in range(m):
    q.append(list(map(int,input().split())))
presum=[arr[0]]
for i in range(1,len(arr)):
    presum.append(presum[i-1]+arr[i])
for i in range(m):
    if q[i][0]==0:
        print(presum[q[i][1]])
    else:
        print(presum[q[i][1]]-presum[q[i][0]-1])