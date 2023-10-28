'''
Instructions:
Stack: Reverse String (⚡Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.
'''

def reverse_string(s):
    stack=[]
    reversed_string=''

    for i in s:
        stack.append(i)
    while stack:
        reversed_string+=stack.pop()
    return reversed_string

print(reverse_string('123456789'))