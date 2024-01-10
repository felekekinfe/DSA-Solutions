

def func(n):
    while True:
        n+=1
        if len(set(str(n)))==len(str(n)):
            return n
n=int(input())
print(func(n))