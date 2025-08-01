stock=list(map(int,input().split()))
n=len(stock)
s=[n-1]
ans=[-1]
for i in range(n-2,-1,-1):
    while s and stock[s[-1]]<=stock[i]:
        s.pop()
    if not s:
        ans.append(-1)
        s.append(i)
    else:
        ans.append(stock[s[-1]])
        s.append(i)
print(ans[::-1])