
def insert(self,value):
    new_node=Node(value)
    if self.root==None:
        self.root=new_node
        return True
    
    temp=self.root

    while True:
        if new_node.value==temp.value:
            return False
        if new_node.value>temp.value:
            if temp.right==None:
                temp.right=new_node
                return True
            temp=temp.right
        else:
            if temp.left ==None:
                temp.left=new_node
                return True
            temp=temp.left
