
def decimaltobinary(n):
    b=''
    
    while n>=1:
        r=n%2
        n=n//2
        b=b+str(r)
    return b

print(decimaltobinary(6))