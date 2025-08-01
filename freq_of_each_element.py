arr=list(map(int,input().split()))
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
        print('element:',i,', Freq:',d[i])
print("Another method to display in one line:")
for i in d:
     print(i,':',d[i],end="  ")