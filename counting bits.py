

def decimaltobinary(n):
    b=''
    
    while n>=1:
        r=n%2
        n=n//2
        b=b+str(r)
    return b
def count_bit(n):

    ans=[]
    for i in range(n+1):
        c=0
        b=decimaltobinary(i)
        for i in b:
            if i=="1":
                c+=1
        ans.append(c)
    return ans

print(count_bit(2))

x=0