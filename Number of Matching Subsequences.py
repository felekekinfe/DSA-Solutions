
def number_of_matching_subsequence(s,words):
    global c
    c=0



    def is_subsequence(s,t):
        if len(t)>len(s):
            pass
        if len(t)==0:
            c+=1
        pt=0
        global c

        for i in range(len(s)):
            if pt<=len(t)-1:
                if t[pt]==s[i]:
                    pt+=1
        if pt==len(t):
            c+=1
    for i in words:
        is_subsequence(s, i)
    return c
print(number_of_matching_subsequence("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

