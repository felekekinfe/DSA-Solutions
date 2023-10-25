

def is_subsequence(s,t):
    
    if len(s)>len(t):
        return False
    if len(s)==0:
        return True
    
    ps=0
    for i in range(len(t)):
        if ps<=len(s)-1:
            if s[ps]==t[i]:
                ps+=1
    if ps==len(s):
        return True
    else:
        return False
 
                
            
    
print(is_subsequence('abc', "ahbgdc"))
