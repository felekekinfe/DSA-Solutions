
def func(arr):
    a=arr[0]
    b=arr[1]
    
    if (a+b)%2==1:
        return 'Alice'
    return 'Bob'


t=int(input())
for i in range(t):
    n=list(map(int,input().split()))

    print(func(n))
