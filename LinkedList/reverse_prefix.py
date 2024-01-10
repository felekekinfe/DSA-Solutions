
def reversePrefix(word: str, ch: str):
        
    ls=word.split()
    l=0
    r=word.index(ch)
    

    
    
    while l<r:
        ls[r],ls[l]=ls[l],ls[r]
        l+=1
        r-=1
    s=''
    for i in ls:
        s+=i
    return s
print(reversePrefix('abcd','c'))