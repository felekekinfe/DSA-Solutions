a=int(input())
b=int(input())
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(a,b))
