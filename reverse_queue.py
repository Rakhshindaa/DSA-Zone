def reverseQueue(q):
    s=[]
    while q:
        s.append(q[0])
        q=q[1:]
    while s:
        q.append(s[-1])
        s.pop()
    return q
q=list(map(int,input().split()))
print(reverseQueue(q))