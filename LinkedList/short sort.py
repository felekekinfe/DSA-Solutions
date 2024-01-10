def x(arr):
    if arr=='abc':
        return 'Yes'
    l=0

    for i in range(2):
        x=list(arr)
        x[i],x[i+1]=x[i+1],x[i]
        if x==list('abc'): 
            return 'Yes'
    x=list(arr)
    x[l],x[2]=x[2],x[l]
    if x==list('abc'):
        return 'Yes'
    return 'No'

t=int(input())
for i in range(t):
    arr=input()
    print(x(arr))




            
        


