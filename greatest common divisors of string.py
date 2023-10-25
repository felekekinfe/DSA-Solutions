



def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def gcd_of_string(str1,str2):
    w1=str1+str2
    w2=str2+str1
    if w1==w2:
        x=gcd(len(str1),len(str2))
        return w1[0:x]
    else:
        return ""
print(gcd_of_string("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))


min=min()