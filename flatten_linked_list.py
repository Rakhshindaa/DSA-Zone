class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.bot=None
def create_list():
    n00=Node(5)
    n01=Node(7)
    n02=Node(8)
    n03=Node(30)
    n10=Node(10)
    n11=Node(20)
    n20=Node(19)
    n21=Node(22)
    n22=Node(50)
    n30=Node(28)
    n31=Node(35)
    n32=Node(40)
    n33=Node(45)
    #linking the next nodes
    n00.next=n10
    n10.next=n20
    n20.next=n30
    #linking bottom nodes
    n00.bot=n01
    n01.bot=n02
    n02.bot=n03
    n10.bot=n11
    n20.bot=n21
    n21.bot=n22
    n30.bot=n31
    n31.bot=n32
    n32.bot=n33
    head1=n00
    head2=n10
    head3=n20
    head4=n30
    return head1
def display_list(head):
    curr=head
    while curr:
        curr1=curr
        while curr1:
            print(curr1.val,end='-> ')
            curr1=curr1.bot
        print()
        curr=curr.next
    print()
def display_flist(head):
    curr=head
    while curr:
        print(curr.val,end=' ')
        curr=curr.next
    print()
def flatten(head):
    d=Node(None)
    p=d
    curr=head
    while curr and curr.next:
        cur1=head
        cur2=head.next
        while cur1 and cur2:
            if cur1.val<cur2.val:
                p.next=Node(cur1.val)
                cur1=cur1.bot
            else:
                p.next=Node(cur2.val)
                cur2=cur2.next
            p=p.next
        while cur1:
            p.next=Node(cur1.val)
            cur1=cur1.bot
            p=p.next
        while cur2:
            p.next=Node(cur2.val)
            cur2=cur2.bot
            p=p.next
        curr=curr.next
    return d.next
head1=create_list()
display_list(head1)
ans=flatten(head1)
display_flist(ans)