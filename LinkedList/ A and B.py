c=0
a=20
b=30
a=min(a,b)
b=max(a,b)
for i in range(1,max(a,b)+1):
    if b==a:
        print(c)
        break
    if i%2==0:
        b+=i
        c+=1
        if b==a:
            print(c)
            break
    else:
        a+=i
        c+=1
        if b==a:
            print(c)
            break
