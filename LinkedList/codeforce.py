


def gcd_max(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd_max(b, a % b)
    








t=int(input())
nums=[]
for i in range(t):
    f=int(input())
    nums.append(f)
maxx=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        gcd=gcd_max(nums[i],nums[j])
        maxx=max(maxx,gcd)
print(maxx)
