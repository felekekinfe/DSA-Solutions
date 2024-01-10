
def func(a,t):
    l=0
    r=len(a)-1
    x=[]
    while l<r:
        m=(l+r)//2

        if a[m]==t:
            x.append(m)
            l=m+1
        elif a[m]>t:
            r=m-1
        else:
            l=m+1
    print(x)
func([1,2,2,2,3], 2)

