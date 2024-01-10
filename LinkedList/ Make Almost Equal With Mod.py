def func(arr):
    x=[]
    y={}
    for i in range(1,max(arr)+1):
        for j in arr:
            x.append(j%i)
        for k in x:
            if k not in y:
                y[k]=1
            else:
                y[k]+=1
        for b,v in y.items():
            if v==2:
                return i+5

print(func([60 ,90 ,98 ,120 ,308]))
