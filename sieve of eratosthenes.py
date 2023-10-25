

def sieve_prime(n):
    unmark=[False for i in range(n)]
    for i in range(2,n):
        if unmark[i]==False:
            for j in range(2*i,n,i):
                unmark[j]=True
    for i in range(2,len(unmark)):
        if unmark[i]==False:
            print(i)
    
    return unmark

print(sieve_prime(50))