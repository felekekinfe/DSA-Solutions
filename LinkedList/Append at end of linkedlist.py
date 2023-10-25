
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def printLinkedlist(self):
        temp=self.head

        while temp is not None:
            print(str(temp.value) + "-->", end='')
            temp=temp.next



    #apppend element to the end

    def append(self,value):
        add_node=Node(value)
        if self.length==0:
            self.head=add_node
            self.tail=add_node
        else:
            self.tail.next=add_node
            self.tail=add_node
        self.length+=1


        #add element at the front
    def prepend(self,value):
        add_node=Node(value)
        
        if self.length==0:
            self.head=add_node
            self.tail=add_node
        else:
            current_head=self.head
            self.head=add_node
            self.head.next=current_head
        self.length+=1

        #get element by their index(position),index=0,1,2,3...

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        elif index==0:
            return self.head
        elif index==self.length-1:
            return self.tail.value
        else:
            current_head=self.head
            for _ in range(index):
                current_head=current_head.next
            return current_head.value
    def set_value(self,index,value):
        if index<0 or index>=self.length:
            return None
        elif index==0:
            self.head.value=value
        elif index==self.length-1:
            self.tail.value==value
        else:
            current_head=self.head

            for _ in range(index):
                current_head=current_head.next
            current_head.value=value


            #insert element at a particular possitions(index)
    def insert(self,index,value):
        new_node=Node(value)
        if index<0 or index>=self.length:
            return None
        elif index==0:
            current_head=self.head
            self.head=new_node
            self.head.next=current_head
        elif index==self.length-1:
            self.tail.next=new_node
            self.tail=new_node
        else:
            current_head=self.head
            for _ in range(index-1):
                current_head=current_head.next
            temp=current_head.next
            current_head.next=new_node
            current_head=new_node
            current_head.next=temp
        







  
                
    #remove from the last
    def pop(self):
        if self.length==0:
            return None
        
        temp=self.head
        pre=temp

        while temp.next:
            pre=temp
            temp=temp.next

        self.tail=pre
        self.tail.next=None
        self.length-=1
        
        if self.length==0:
            self.tail=None
            self.head=None
    
    #delete element from particular position(index)

    def remove(self,index):

        
        if index<0 or index>=self.length:
            return None
        elif index==0:
            self.head=self.head.next
            
        else:
            temp=self.head
            pre=temp

            for _ in range(index):
                pre=temp
                temp=temp.next

            pre.next=None
            t1=temp.next
            temp.next=None
            pre.next=t1
            
            self.length-=1

            if self.length==0:
                self.head=self.tail=None


            


      

        

        


        
        
        
        
        
        
        
        
            

        

l=LinkedList(1)




l.append(2)
l.append(3)

l.prepend(0)
l.remove(0)
print(l.get(4))
l.printLinkedlist()