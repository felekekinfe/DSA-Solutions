

def count_vowel(s):
    v=['a','i','u','e','o']
    s=set()
    c=0
    l=0
    r=1

    for i in range(len(s)-1):
        while l<=r:
            if s[l] in v and s[r] in v:
                if s[l]!=s[r]:
                    l+=1
                    r+=1
                    c+=1
                else:
                    l+=1
                    r+=1
                