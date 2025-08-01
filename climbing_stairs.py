n=int(input())
steps=[1]*(n+1)
for i in range(2,n+1):
    steps[i]=steps[i-1]+steps[i-2]
print(steps[n])