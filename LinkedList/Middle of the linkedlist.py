

def middle_of_linkedList(self,head):
    
    c=0
    current_head=head

    while current_head:
        c+=1
        current_head=current_head.next

    mid=c//2
    temp=head
    pre=temp


    for _ in range(mid):
        pre=temp
        temp=temp.next
    pre=None

    return temp

    