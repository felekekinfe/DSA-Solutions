def makeGood(s):


    st=[]

    if len(s)==1:
        return s

    for i in s:
        if not st:
            st.append(i)
        else:
            if st[-1]==i.lower() and i!=i.lower():
                st.pop()
            else:
                st.append(i)
    ans=''

    for i in st:
        ans+=i
    return ans

print(makeGood("abBAcC"))


