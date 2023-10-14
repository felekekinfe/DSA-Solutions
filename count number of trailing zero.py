
def trailing_zero(n):
    c=0
    while n%10==0:
        n=n//10
        c+=1
    return c



    
print(trailing_zero(1090))