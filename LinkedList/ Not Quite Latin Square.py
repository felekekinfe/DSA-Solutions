


def func(mtrx):
    x=0
    for r in mtrx:
        for e in r:
            if e=='?':
                

                x=r
    for i,k in enumerate('ABC'):
        if k not in x:
            return k



        

t=int(input())
for i in range(t):
    s1=list(input())
    s2=list(input())
    s3=list(input())
    mtrx=[s1,s2,s3]
    print(func(mtrx))