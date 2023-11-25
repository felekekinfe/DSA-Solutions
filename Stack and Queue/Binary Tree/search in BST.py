

def search(self,value):
    temp=self.root

    while temp is not None:
        if value>temp.value:
            temp=temp.right
        elif value<temp.value:
            temp=temp.left
        else:
            return True
    return False
v=4
s2=[]
s1=[4,1,2,3]
s2=[3,2,1]


    
