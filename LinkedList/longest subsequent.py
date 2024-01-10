

def Lsubsequent(nums):
    m=0

    for l in range(len(nums)-1):
        p=l
        c1=1
        for r in range(l+1,len(nums)):
            if nums[p]<nums[r]:
                c1+=1
                p=r
        m=max(m,c1)
    return m

print(Lsubsequent([0,1,0,3,2,3]))