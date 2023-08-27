
pattern=input()
text=input()
def string_matching(t,p):
    for i in range(len(t)-len(p)+1):
        j=0
        try:
            
            while p[j]==t[i+j]:
                j=j+1
        except:
            if j==len(p):
                return i+1

print(string_matching(text, pattern))