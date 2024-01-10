def maxProfit(prices):

    m=0

    for i in range(len(prices)):
        
        for j in range(i+1,len(prices)):
            p=prices[i]
            p-=prices[j]
            m=min(m,p)
    return abs(m)

print(maxProfit([7,1,5,3,6,4]))
    