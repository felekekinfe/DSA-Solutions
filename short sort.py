
def func(s):
    if s=='abc':
        return "yes"
    
    for i in range(1,len(s)):
        x=list(s)
        x[0],x[i]=x[i],x[0]
        if x==list('abc'):
            return "yes"
    x=list(s)
    x[1],x[2]=x[2],x[1]
    if x==list('abc'):
        return 'yes'
    return 'no'


t=int(input())
for i in range(t):
    s=input()

    print(func(s))