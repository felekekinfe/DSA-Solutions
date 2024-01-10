

def func(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,v in d.items():
        if v==1:
            return i


t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    print(func(arr))