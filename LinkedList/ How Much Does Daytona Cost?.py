
def func(arr,k):
    s=list()
    for i1,i in enumerate(arr):
        c=0
        if i==k:
            s=arr[i1:]
            for j in s:
                if j==k:
                    c+=1
            s.append(c)
    if s and max(s)>0:
        return 'yes'
    return 'no'















t=int(input())
for i in range(t):
    n=list(map(int, input().split()))
    k=n[1]
    arr=list(map(int, input().split()))
    print(func(arr,k))