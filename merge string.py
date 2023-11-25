def mergeAlternately(word1, word2):
    s=''
    x=[]
    c=0
    while c<len(min(word1,word2)):
        s+=word1[c]
        s+=word2[c]
        c+=1
    if len(word1)==len(word2):
        return s
    mx=max(word1,word2)
    s+=mx[c:]

    return s
    
print(mergeAlternately('ac', 'b'))
