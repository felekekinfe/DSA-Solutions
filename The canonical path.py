'''Given a path. the canonical path have the following format:
1.start with '/'
2.any two directories are separated by a single '/'
3.doesnt end with a trailing '/'
4.only contains the directories on the path from the root directory to the
target file or directory(i.e no period '.' or double period '..')

*Given a path, return the canonical path.

Input: path= "/../"
Output: "/"

Input: path= "/home//foo"
Output: "/home/foo"



'''



def solution(path):
    
    stack=[]
    for i in path.split('/'):
        if i=='' or i=='.':
            stack=stack
        elif i=='..' and len(stack)!=0:
            stack.pop()
        else:
            stack.append(i)
    
    return '/'+'/'.join(stack)

print(solution('/h//k/../c/.////k/../'))


