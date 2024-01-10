
import math
def func(arr):
    s=0
    for i in arr:
        s+=i
   
    if math.sqrt(s).is_integer():
        return 'yes'
    return'no'

t=int(input())
for i in range(t):
    a=int(input())
    arr=list(map(int, input().split()))
    print(func(arr))