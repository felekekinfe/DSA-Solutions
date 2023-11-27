def containsdupilicate(nums):
    f={}

    for i in nums:
        x=str(i)

        if x not in f:
            f[x]=1
            if f[x]>=2:
                return True
        else:
            f[x]+=1
            if f[x]>=2:
                return True
            f[x]+=1
    return False

print(containsdupilicate([1,22,2,4,5,6,7,8]))