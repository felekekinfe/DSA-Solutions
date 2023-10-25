
def reverse(n):
    s=str(n)
    x=[]
    for i in s:
        x.append(i)
    l=0
    r=-1
    for i in range(len(x)//2):
        temp=x[r]
        x[l]=temp
        x[r]=x[l]
        l+=1
        r-=1
    print(x)
        

reverse(32)