
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
x=LinkedList(5)
print(x.head.value)