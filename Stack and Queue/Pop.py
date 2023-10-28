
def pop(self):
    if self.top==None:
        return None
    else:
       temp=self.top
       self.top=self.top.next
       temp.next=None
       self.height-=1
       return temp