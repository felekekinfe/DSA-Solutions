
def decimaltobinary(n):
    b=''
    
    while n>=1:
        r=n%2
        n=n//2
        b=str(r)+b
    return b
print(decimaltobinary(1))