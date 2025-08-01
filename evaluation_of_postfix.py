exp=input().split()
s=[-1]
for ch in exp:
    if ch=='+' or ch=='-' or ch=='/' or ch=='*':
        a=int(s.pop())
        b=int(s.pop())
        if ch=='+':
            s.append(b+a)
        elif ch=='-':
            s.append(b-a)
        elif ch=='*':
            s.append(b*a)
        elif ch=='/':
            s.append(b/a)
    else:
        s.append(ch)
print(s[-1])