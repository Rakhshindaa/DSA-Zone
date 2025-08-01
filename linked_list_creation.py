class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def demo():
    l1=Node(10)
    l2=Node(20)
    l3=Node(30)
    l4=Node(40)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    temp=l1
    while temp:
        print(temp.val,end=' ')
        temp=temp.next
def Create_list(ar):
    head=Node(ar[0])
    curr=head
    for i in ar[1:]:
        curr.next=Node(i)
        curr=curr.next
    return head
def display_list(head):
    curr=head
    while curr:
        print(curr.val,end=' ')
        curr=curr.next
    print()
def insert_start(head,x):
    new=Node(x)
    new.next=head
    head=new
    return head
def insert_nth(n,x,head):
    count=0
    temp=head
    new=Node(x)
    while count<n-2:
        count+=1
        temp=temp.next
    new.next=temp.next
    temp.next=new
def insert_end(head,x):
    new=Node(x)
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new
def delete_start(head):
    head=head.next
    return head
def delete_nth(n,head):
    temp=head
    count=0
    while count<n-2:
        count+=1
        temp=temp.next
    temp.next=temp.next.next
    return head
def delete_end(head):
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head
ar=list(map(int,input('Enter values: ').split()))
head=Create_list(ar)
display_list(head)
print()
ch=1
while ch!=0:
    print('1. insert at start\n2. insert at nth position\n3. insert at end')
    print('4. delete at start\n5. delete at nth position\n6.delete at end\n0. exit\n')
    ch=int(input('enter operation:'))
    if ch==1:
        x=int(input("enter the value:"))
        head=insert_start(head,x)
        display_list(head)
        print()
    elif ch==2:
        pos,x =map(int,input('enter the position and the value:').split())    
        insert_nth(pos,x,head)
        display_list(head)
    elif ch==3:
        x=int(input("enter the value:"))
        insert_end(head,x)
        display_list(head)
    elif ch==4:
        head=delete_start(head)
        display_list(head)
    elif ch==5:
        pos=int(input('enter the position to delete :'))    
        delete_nth(pos,head)
        display_list(head)
    elif ch==6:
        delete_end(head)
        display_list(head)
    elif ch==0:
        exit()
    else:
        print("\nInvalid choice...select again\n")