
def is_subsequence(s,t):
    ps=0
    pt=0

    while ps<len(s):
        if s[ps]==s[pt]:
            ps+=1
            pt+=1
        else:
            pt+=1
    if ps==len(s):
        return True
    return False
print(is_subsequence("axc", "ahbgdc"))
    