exp=input().split()
ans=[]
s=[]
sym={'+':1,'-':1,'*':2,'/':2,'%':2,'**':3}
for ch in exp:
    if ch=='+' or ch=='-' or ch=='/' or ch=='*' or ch=='**' or ch=='%':
        if not s:
            s.append(ch)
        elif sym[ch]>=sym[s[-1]]:
            s.append(ch)
        elif sym[ch]<sym[s[-1]]:
            ans.append(s.pop())
    elif ch=='(':
        s.append(ch)
    elif ch==')':
        while s[-1]!='(':
            ans.append(s.pop())
        s.pop()
    else:
        ans.append(ch)
print(ans)