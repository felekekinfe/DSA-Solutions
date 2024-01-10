def fun(m):
    x=''
    m=sorted(m)
    
    c=0
    for i in m:
        x+=i
        if c<len(m)-1:

            x+="+"
            c+=1
        
    return x


t=input()

m=t.split('+')

print(fun(m))