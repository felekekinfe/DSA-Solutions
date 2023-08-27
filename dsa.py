# n,m=input().split()
# def gcd(n,m):
#     while m!=0:
#         return gcd(m,n%m)
#     return n

# print(gcd(int(n),int(m)))



# t=int(input())


# def odd(n):
#     for i in range(2,1,n):
#         if i%2!=0:
#             if n%i==0:
#                 return 'yes'
#                 break





# def testcase():
#     c=t
# #     for i in range(c):
# #         n=int(input())
# #         print(odd(n))
# # testcase()

# t2=int(input())


# def nplusm(n):
#     for i in range(2,n+1):
#         if(n+i)%2!=0 and (n+i)%i!=0:
#             print(n+i)
#             break
            
# def testcase():

#     for i in range(t2):
#         n=int(input())
#         nplusm(n)
# testcase()
#

# def find_prime_sum(t, test_cases):
#     for _ in range(t):
#         n = test_cases[_]
#         m = 2
#         while True:
#             if is_prime(n + m):
#                 break
#             m += 1
#         print(m)

# # Get input from the user
# t = int(input("Enter the number of test cases: "))
# test_cases = []
# for _ in range(t):
#     n = int(input("Enter a prime number: "))
#     test_cases.append(n)

# # Call the function
# find_prime_sum(t, test_cases)





# def merge(a):
#     x=len(a)
#     m=x//2
#     if x>1:
#         l=a[:m]
#         r=a[m:]
#         merge(l)
#         merge(r)
#         k=i=j=0

#         while i<len(l) and j<len(r):
#             if l[i]<r[j]:
#                 a[k]=l[i]
# #                 i+=1
# #             else:
# #                 a[k]=r[j]
                
# #                 j+=1
# #     return a
# # print(merge([4,3,2]))




# def sub(s):
#     l=0
#     r=l+1
#     c=0
#     x=[]
#     h={}
#     for i in range(len(s)):
#         if s[l]!=s[r] and s[l] not in h:
#             c=c+1
#             l=l+1
#             c=c+1
#         else:
#             x.append(c)
#             c=0
#     return x
# print(sub('abca'))

# def climb(n):
#     x,y=1,1
#     for i in range(n-1):
#         t=x
#         x=x+y
#         y=t
#     return x
# print(climb(3))

# def cost_climb(n):
#     c=0
#     l=0
#     r=1
#     for i in range(len(n)-1):
#         if n[l]<n[r]:
#             c=c+n[l]
#             l=r
#             r=r+l
#         else:
#             l=r+1
#             r=l+1
#     return c
# print(cost_climb([100,15,20]))



# import math

# def solution(x: int, z: int) -> [int]:
    
#     res = []
#     a=[]
#     y=[]
#     for i in range(x,z+1):
#         a.append(i)
#     for i in range(len(a)):
#         if len(str(a[i]))==1:
#             res.append(a[i])
#         else:
#             for j in str(a[i]):
#                 try:
#                     if len(str(a[i])) >1 and a[i]%int(j)==0:
#                         res.append(a[i]) 
#                 except ZeroDivisionError:
#                     pass

                        



#     return res
# print(solution(1, 22))



# def neg_pos_zero():
#     nums=input().split()
#     for i in nums:
#         try:
#             i=int(i)
#             if i>0:
#                 print('Positive')
#             elif i<0:
#                 print('negative')
#             elif i==0:
#                 print("Zero")
#         except:
#             print("Invalid Type")
# print(neg_pos_zero())

#Turing coding challenge................................................
# def perfect_integer():
#     p_nums=[]
#     x,y=input().split()
#     x,y=int(x),int(y)
    
#     for i in range(x,y+1):
#         if len(str(i))==1:
#             p_nums.append(i)
#         else:
            
#             x=0
#             for j in str(i):
                
#                 try:
                    
#                     if i%int(j)==0 and i not in p_nums:
#                         x+=1
#                         if x==len(str(i)):
#                             p_nums.append(i)
                            
                
                    
#                 except:
#                     pass
#     return p_nums
# print(perfect_integer())     
                







def knapsack(w,v,c):
    n=len(v)
    sack=[]
    count=0
    val=0
    
    for i in range(len(w)-1):
        for j in range(1,len(w)-2):
            if count<c:
                count=w[i]+w[j]+count
                val=val+c[i]+c[j]
                c=c-count

            else:
                sack.append(val)
                count=0
    print(sack)

knapsack([1,2,3], [3,2,1], 130)
