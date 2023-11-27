def majorityElement(nums):

    f={}

    for i in nums:
        if str(i) not in f:
            x=str(i)
            f[x]=1
        else:
            x=str(i)
            f[x]+=1
    c=len(nums)/2

    for i in f:
        if f[i]>c:
            return int(i)
print(majorityElement([3]))