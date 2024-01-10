# def winner(a,k):
#     i=0
#     size=len(a)
#     while size>1:
#         i=(i+k-1)%size
#         del a[i]
#     return a[0]
# print(winner([1,2,3,4,5], 2))

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
# for row_idx in range(len(matrix)):
#     for col_idx in range(len(matrix[0])):
#         print(matrix[row_idx][col_idx])

# for row_idx in range(len(matrix) - 1, -1, -1):
#     for col_idx in range(len(matrix[0]) - 1, -1, -1):
#         print(matrix[row_idx][col_idx])

# for i in range(len(matrix)):
#     if i%2==0:
#         for j in range(len(matrix[i])):
#             print(matrix[i][j])
#     else:
#         for j in range(len(matrix[i])-1,-1,-1):
#             print(matrix[i][j])

x1={}
nums=[0,0,1,0]
for i in range(len(nums)+1):
    s=0
    nl=nums[:i]
    nr=nums[i:]

    if nl.count(0)+nr.count(1)>=s:
        s=nl.count(0)+nr.count(1)
        if i in x1:
            x1[i]+=s
        else:
            x1[i]=s
a=[i for i in x1 if x1[i]==max(x1.values())]
print(a)