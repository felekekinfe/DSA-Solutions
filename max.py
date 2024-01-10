m=0
n="12"
for i,k in enumerate(n):
    x=list(n)
    if k=='1':
        del x[i]
        m=max(m,int(''.join(x)))
print(m)