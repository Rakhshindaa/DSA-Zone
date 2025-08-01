stock=list(map(int,input().split()))
n=len(stock)
s=[0]
print(-1,end=' ')
for i in range(1,n):
    while s and stock[s[-1]]<=stock[i]:
        s.pop()
    if not s:
        print(-1,end=' ')
        s.append(i)
    else:
        print(stock[s[-1]],end=' ')
        s.append(i)