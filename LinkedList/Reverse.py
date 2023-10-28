
def reverse(self):
    temp=self.head
    self.head=self.tail
    self.tail=temp

    before=None
    after=temp.next

    for _ in range(self.length):
        after=temp.next
        temp.next=before
        before=temp
        temp=after
        