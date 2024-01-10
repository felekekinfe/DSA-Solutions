

def maxsubK(nums,k):
    m=0
    for i in range(len(nums)):
        s=0
        for j in range(i,len(nums)):
            s+=nums[j]
            if k==s:
                m+=1
    return m

print(maximumAverage([1,1,1],2))