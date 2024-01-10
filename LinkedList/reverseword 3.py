
def reverse_word(s):
    
    re=[]
    s=s.split()
    for i in s:
        re.append(i[::-1])
       
        
    return ' '.join(re)
print(reverse_word("let's take leetcode contest"))