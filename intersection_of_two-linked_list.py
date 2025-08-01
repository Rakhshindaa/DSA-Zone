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
def intersection(head1,head2):
    d=Node(None)
    ans=d
    val2=set()
    curr=head2
    while curr:
        val2.add(curr.val)
        curr=curr.next
    curr=head1
    while curr:
        if curr.val in val2:
            d.next=Node(curr.val)
            d=d.next
        curr=curr.next
    return ans.next
l1=list(map(int,input('Enter values: ').split()))
head1=Create_list(l1)
l2=list(map(int,input('Enter values: ').split()))
head2=Create_list(l2)
print('linked list 1:')
display_list(head1)
print('linked list 2:')
display_list(head2)
print('intersection of two linked lists:')
ans=intersection(head1,head2)
display_list(ans)