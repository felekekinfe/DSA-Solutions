
def func(n):
    if n%2==0:
        for i in range(1,n+1):
            print(2*i, end=' ')
    else:
        for i in range(1,n+1):
            print(i, end=' ')
t=int(input())
for i in range(t):
    n=int(input())
    func(n)