
class Node:
    def __init__(self,value):
        self.head=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


LinkedList(4)

