
def prime_factor(n):
    x=2
    while n>1:
        while n%x==0:
            
            print(x)
            n=n//x
        x+=1

    

print(prime_factor(130))
