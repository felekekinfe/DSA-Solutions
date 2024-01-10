def simplifyPath(path: str):

    stack=[]

    for i in path:
        
        if stack and i==stack[-1]=='/':
                pass
        elif i=='.' or i=='..':
            pass
        else:
            stack.append(i)
    if stack[-1]=='/':
        del stack[-1]
    path=''.join(stack)
    
    return path
print(simplifyPath("/home//foo/"))