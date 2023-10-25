
def countBits(n):
    ans=[]
    
    def decimaltobit(x):
        b=''
        while x>=1:
            r=x%2
            x=x//2
            b=str(r)+b
        return b
        
    for i in range(n+1):
        c=0
        y=decimaltobit(i)

        for i in y:
            if i=='1':
                c+=1
        ans.append(c)
    return ans


print(countBits(2))




       

