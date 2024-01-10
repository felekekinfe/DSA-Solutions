
from array import array
def func(arr):
    l=0
    s=array('i',list(map(int,list(arr))))
    r=len(s)-1
    
    
    while l<r:
        if s[l]!=s[r]:
            del arr[0]
            del arr[len(arr)-1]

            l+=1
            r-=1
        else:
            return len(arr)
    return len(arr)


t=int(input())

for i in range(t):
    l=int(input())
    arr=input()
    print(func(list(arr)))
