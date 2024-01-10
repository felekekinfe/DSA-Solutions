
def fun(m):

    mi=1
    mj=1

    for i,k1 in enumerate(m):
        for j,k2 in enumerate(k1):
            
            if m[i][j]=='1':
                mi=i+1
                mj=j+1
                return abs((3-mi)+(mj-3))
    
    







m=[]
for i in range(5):
    e=input().split()
    m.append(e)
print(fun(m))