
def func(x):
    c=0
    for i in x:
        if '+' in i:
            c+=1
        else:
            c-=1
    return c





n=int(input())
x=[]
for i in range(n):
    a=input()
    x.append(a)
print(func(x))