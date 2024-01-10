def stack_remove(s):
    if len(s)%2==0:
        del(s[len(s)//2-1])
    else:
        del(s[len(s)//2])
    return s
print(stack_remove([1,2,3]))