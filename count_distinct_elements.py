arr=list(map(int,input().split()))
d={}
count=0
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
        count+=1
print("Unique elements=",count)
print("The unique elements are:")
for i in d:
    if d[i]==1:
        print(i,end=' ')