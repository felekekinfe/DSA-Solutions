
def func(arr):
    m=float('inf')
    inx=0
    for i,k in enumerate(arr):
        if k<m:
            m=k
            inx=i 
    arr[inx]=arr[inx] +1
    p=1
    for i in arr:
        p*=i
    return p







t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    print(func(arr))