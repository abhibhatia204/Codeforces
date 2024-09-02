n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
b=10000000
for i in range(1,k-n):
    c=min(b,a[i+n-1] - a[i])
print(c)
# a.sort()
# p=[]
# cnt=1
# for i in range(0,len(a)):
#     c=set(a)
#     if(len(c)==1):
#         print("0")
#     else:
#         z=a[len(a)-cnt] - a[i]
#         if(z>=0):
#             p.append(z)
#         cnt+=1
# p.sort()
# print(p)