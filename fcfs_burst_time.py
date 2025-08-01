n=int(input())
b=list(map(int,input().split()))
a=list(map(int,input().split()))
q=[]
total_time=0
p=range(n)
order=sorted(zip(a,p))
print(order)
for i,j in order:
    total_time+=b[j]
    q.append(j)
print(q)
print(total_time)