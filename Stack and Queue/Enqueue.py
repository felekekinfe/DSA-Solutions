

def enqueue(self,value):
    new_node=Node(value)

    if self.first is None:
        self.first=new_node
        self.last=new_node
    else:
        self.last.next=new_node
        self.last=new_node
    self.length+=1
