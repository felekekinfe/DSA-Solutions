
class Stack:
    def __init__(self,stack):
        self.stack=stack
    def push(self,value):
        self.value=value
        self.stack.append(self.value)

        return self.stack
    def top(self):

        return self.stack[-1]
    
    def pop(self):
        self.stack.pop()

        return self.stack
    
    def getmin(self):
        return min(self.stack)

s=Stack([1,2,3,5])
print(s.push(8))