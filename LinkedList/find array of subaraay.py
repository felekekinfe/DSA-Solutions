
def sub_array(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            print(nums[i:j+1])

sub_array([0,2,3,4,5])