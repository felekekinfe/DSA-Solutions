'''Instructions:
Stack: Parentheses Balanced (⚡Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.'''



def is_balanced_parentheses(s):
    stack=[]

    for i in s:
        if len(stack)==0 and i !=')':
            stack.append(i)
        else:
            if i==')' and '(' in stack:
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        return "balanced"
    return 'unbalanced'
print(is_balanced('((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))'))