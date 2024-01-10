

def func(s):
    n=s[0]
    for i in range(1,len(s)):
        if s[i]!='0':
            if int(n)<int(s[i:]):
                return print(int(n),int(s[i:]))
                
            else:
                return -1
        else:
            n+=s[i]
            


t=int(input())

for i in range(t):
    s=input()
    print(func(s))