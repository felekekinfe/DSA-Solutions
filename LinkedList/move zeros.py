def move_zeros(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
    return nums

print(move_zeros([1,0,3,0,2]))

l=0
r=1

for i in range(len(nums)):
    if nums[l]==0:
        nums[l],nums[r]=nums[r],nums[l]
        r+=1
    else:
