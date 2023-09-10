'''Given a string x of only brackets.

Return true if x is valid and false otherwise.

.Input: ({}[])
.Output: true

.Input: ({)
.Output: false

'''

def isValid(x):
    stack=[]
    mapping={
             '}':'{',
             ')':'(',
             ']':'['
             }
    for i in range(len(x)):
        if x in '([{':
            stack.append(x)
        else:
            if stack:
                if mapping(x)==stack[-1]:
                    stack.pop()
    if len(stack)==0:
        return True
    else:
        return False
print(isValid('({})'))




    # for i in x:
    #     if len(stack)==0:
    #         stack.append(i)
    #     elif stack[-1]=='{' and i=='}':
    #         stack.pop()
    #     elif stack[-1]=='[' and i==']':
    #         stack.pop()
    #     elif stack[-1]=='(' and i==')':
    #         stack.pop()
    #     else:
    #         stack.append(i)
    # if len(stack)==0:
    #     return True
    # else:
    #     return False
    


            
