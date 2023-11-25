def countPrimes(n):
   

    def is_prime(a):
        if a==4:
            return False

        for i in range(2,(a+1)//2):
            if a%i==0:
                return False
        return True
    if n<=2:
        return 0
    x=[]
    c=0

    for i in range(2,n):
        x.append(i)
    
    for i in x:
        ans=is_prime(i)
        if ans:
            c+=1
    return c
    

print(countPrimes(12))