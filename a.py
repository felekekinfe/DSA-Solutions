# def matrix(mat):
#     h={}

#     for r in mat:
#         for e in r:
#             if e in h:
#                 h[e]+=1
#             else:
#                 h[e]=1
#     m=float('inf')

#     for k,v in h.items():
#         if v==len(mat):
#             m=min(k,m)
#     if float('inf')==m:
#         return -1
#     return m
    
# print(matrix([[1,2,9],[4,5,9],[7,8,11]]))

from collections import Counter
mat=[[1,2,9],[4,5,9],[7,8,11]]
x=Counter([i for j in mat for i in j ])

