# def func(arr):
#     c=0
#     if arr[0]==50 or arr[0]==100:
#         return 'NO'
    
#     for i in arr:
#         if i==25:
#             c+=i
        
#         else:
#             x=i-25
#             if c>=x:
#                 c=i-c
            
#         if c==25:
#             return 'YES'
#     return 'NO'




def func(arr):
    s=[]
    for i in arr:
        if i==25:
            s.append(i)
        elif i==50:
            if 25 in s:
                s.remove(25)
                s.append(i)
        else:
            c=0
            for k in range(len(s)-1):
                c=s[k]
                for j in range(k+1,len(s)-1):
                    c+=s[j]
                    if c==75:
                        s.remove(s[k])
                        s.remove(s[j])
                        s.append(i)
    if s[0]==arr[-1]:
        return 'yes'
    return 'no'

                    






n=int(input())
arr=list(map(int,input().split()))
print(func(arr))
