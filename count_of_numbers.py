n=int(input())
arr=list(map(int,input().split()))
pos=0
neg=0
zer=0
for i in range(n):
    if arr[i]>0:
        pos+=1
    elif arr[i]<0:
        neg+=1
    else:
        zer+=1
print("positive:",pos)
print("Negative:",neg)
print("Zeroes:",zer)