def maxProfit(prices):

    m=0
    x=list(set(prices,r))
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i]<x[j]:
                m=max((x[j]-x[i]),m)
    return m

print(maxProfit([7,1,5,3,6,4]))