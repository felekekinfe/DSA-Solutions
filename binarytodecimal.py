
def Binary_to_Decimal(n):
    b=0
    powerof2=1
    c=-1
    for i in range(len(n)):
       
        if n[c]=='1':
            b=b+powerof2
        c-=1
        powerof2=powerof2*2
    return b
print(Binary_to_Decimal('101101'))