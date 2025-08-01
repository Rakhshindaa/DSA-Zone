class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
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
def swappair(head):
    curr=head
    while curr and curr.next:
        curr.val,curr.next.val=curr.next.val,curr.val
        curr=curr.next.next
    return head
ar=list(map(int,input('Enter values: ').split()))
head=Create_list(ar)
print('before swapping:')
display_list(head)
head=swappair(head)
print('after swappinng:')
display_list(head)