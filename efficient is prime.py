
import math

def efficient_is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

print(efficient_is_prime(200000000))