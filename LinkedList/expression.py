
def func(a,b,c):
    m=0
    for i in range(1):
        x=a+b+c
        y=a*b*c
        z=(a+b)*c
        v=a*(b+c)
        m=max(m,x,y,z,v)
        return m



for i in range(1):  
    a=int(input())
    b=int(input())
    c=int(input())

    print(func(a,b,c))

    