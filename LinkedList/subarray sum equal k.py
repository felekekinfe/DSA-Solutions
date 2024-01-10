
def subarray(arr,k):
    t=0
    c=0
    for i in range(len(arr)):
        t=0
        for j in range(j,len(arr)):
            t+=arr[j]
            if k==t:
                c+=1
