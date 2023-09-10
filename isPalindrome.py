def isPalindrome(s):
    s=str(s)
    l=0
    r=-1
    x=True
    for i in s:
        if s[l]!=s[r]:
            x=False
            break
        else:
            l+=1
            r-=1
    return x

print(isPalindrome('12'))#true