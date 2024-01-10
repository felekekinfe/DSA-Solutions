def func(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                if arr[i]%2==0 and arr[j]%2==0:
                    arr[i],arr[j]=arr[j],arr[i]
                if arr[i]%2!=0 and arr[j]%2!=0:
                    arr[i],arr[j]=arr[j],arr[i]
    if arr==sorted(arr):
        return 'yes'
    return 'no'

t=int(input())
for i in range(t):
    n=int(input())

    arr=list(map(int, input().split()))
    print(func(arr))
