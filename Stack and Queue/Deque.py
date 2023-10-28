
def deque(self):
    if self.length==0:
        return None
    elif self.length==1:
        self.first=None
        self.last=None
    else:
        temp=self.first
        self.first=self.first.next
        temp.next=None