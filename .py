

# def runningSum(nums):
#     runningsum=[nums[0]]

#     for i in range(1,len(nums)):
#         if runningsum[:i] not None:
#             for i in range(len(nums[:i])):
                
#     return runningsum

# print(runningSum([1,2,3,4]))


# def quicksort(array):
#     if len(array) < 2:
#         return array 
#     else:
#         pivot = array[0] 
#         less = [i for i in array[1:] if i <= pivot] 
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([13,4,3]))
# def a(candies,extraCandies):
#     r=[]
#     for i in candies:
#             c=0
#             for j in candies:
#                 e=i+extraCandies
#                 if int(e)<int(j):
#                     c=1
#                     r.append('false')
#                     break
#             if c==0:
#                 r.append('true')
#     return r
# print(a([12,1,12],10))
# x=[4,3,2]
# x[0]='t'
# print(x)

# def a(candies,extraCandies):
#     result=[]
#     maxc=max(candies)
#     for i in candies:
#         e=i+extraCandies
#         if e>=maxc:
#             result.append('true')
#         else:
#             result.append('false')
#     return result
    
# print(a([2,3,5,1,3],3)

x=[1,2,3]
y=[4,5]
x[0]=0
print(x)