def findMaxAverage(nums, k):
    msum=0
    s=0
    c=0

    for i in range(len(nums)):
        s=0
        for j in range(i,len(nums)):
            s+=nums[j]
            msum=max(s,msum)
            if s!=msum:
                c+=1
    return msum/c

print(findMaxAverage([1,12,-5,-6,50,3], 4))