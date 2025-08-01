stock=list(map(int,input().split()))
n=len(stock)
s=[0]
print(1)
for i in range(1,n):
    while s and stock[s[-1]]<=stock[i]:
        s.pop()
    if not s:
        print(i+1)
        s.append(i)
    else:
        print(i-s[-1])
        s.append(i)