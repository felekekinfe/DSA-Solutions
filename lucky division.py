


n=int(input())
def luck(n):
    for i in range(1,n+1):
        if str(i) in '47':
            if n%i==0:
                return "YES"
    return "NO"



print(luck(n))


