

def threeSum(arr):
    ans=[]
    for i in range(len(arr)):
        for j in range(1,len(arr)-1):
            for k in range(2,len(arr)-2):
                if arr[i]!=arr[j]!=arr[k] and arr[i]+arr[j]+arr[k]==0:
                    ans.append(i)
                    ans.append(j)
                    ans.append(k)
                    return ans
   +

    return ans

print(threeSum([0,0,0]))