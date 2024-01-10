import  copy
def transpose(matrix):
    x=[[0]*len(matrix) for i in range(len(matrix[0]))]
   
    
    # y=[[0] * len(matrix) for _ in range(len(matrix[0]))]
    # print(y)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            x[j][i]=matrix[i][j]
    
    return x
print(transpose([[1,2,3],
                 [4,5,6]]))

