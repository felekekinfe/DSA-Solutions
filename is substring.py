

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return False
        

        c=0
        for i in range(len(t)):
            if c<=len(s):
                if len(s)==1:
                    if s[c]==t[i]:
                        return True
                        
                else:
                    if s[c]==t[i]:
                        c+=1
        if c==len(s):
            return True
        else:
            return False

        

            
        
           
      

s=Solution()
print(s.isSubsequence('abc', "ahbgdc"))

x=[1,2,3,4]
print(x[5:])

S=[[1,2],[3,4]]
a,b=[1,2]
print(a+b)