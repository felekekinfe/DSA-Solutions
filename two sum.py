


def TwoSum(arr,t):
    l=0
    r=len(arr)-1
    arr=sorted(arr)
    while l<r:
        if arr[l]+arr[r]==t:
            return [arr[l],arr[r]]
        if arr[l]+arr[r]>t:
            r-=1
        else:
            l+=1

    return []

print(TwoSum([2,7,11,15], 9))