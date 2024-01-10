


tlc=list(map(int, input().split()))
card=list(map(int, input().split()))
color=list(map(int, input().split()))
# t=list(t)
# c=list(c)



s=[]


for i,v in enumerate(color):
    for j,k in enumerate(card):
        if v==k:
            s.append(j+1)
            x=k
            del card[j]
            card.insert(0,x)
            break
for i in s:
    print(int(i),end=' ')

