def print_mat(m,n):
    for i in range(n):
        for j in range(n):
            print(m[i][j],end=' ')
        print()
n=int(input())
m=[]
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
print("Before Swapping:")
print_mat(m,n)
for i in range(n):
    m[i][i],m[i][n-i-1]=m[i][n-i-1],m[i][i]
print("After swapping:")
print_mat(m,n)