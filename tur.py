def t(m):
    ans=[]
    for i in range(len(m)-1):
        if m[i]==m[i+1]=='.':
            ans.append('--)


            ans.insert(i,'--'+m[i]+m[i+1])
    return ans

print(t('....'))