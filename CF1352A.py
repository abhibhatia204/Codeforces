x = int(input())
for i in range(x):
    cnt = 0
    p = 0
    z = []
    t = input()
    for j in range(len(t)-1,-1,-1):
        for l in range(p,len(t)):
            if(t[l]!="0"):
                z.append(t[l]+("0" * j))
            p += 1
            break
    print(len(z))
    for q in range(len(z)):
        print(z[q],end=" ")
    print("")






























# x=int(input())
# cnt=1
# for i in range(x):
#     y=int(input())
#     z=str(y)
#     if(len(z)==1):
#        print(cnt)
#        print(y)
#     elif(len(z)==2):
#         if(y%10==0):
#              print(cnt)
#              print(y)
#         else:
#              cnt+=1
#              print(cnt)
#              print((y//10)*10,end=" ")
#              print(y%10)
#     else:
        


























# # a=int(input())
# # cnt=1
# # for i in range(a):
# #     x=int(input())
# #     y=str(x)
# #     if(len(y)==1):
# #         print(cnt)
# #         print(x)
# #     elif(len(y)==2):
# #         if(x%10==0):
# #             print(cnt)
# #             print(x)
# #         else:
# #             cnt+=1
# #             print(cnt)
# #             print((x//10)*10,end=" ")
# #             print(x%10)
# #     else:
#         # while(x!=0):
#         #     cnt+=1
#         #     print((x//10)*10,end=" ")
#         #     print(x%10)
#         #     x=x%10
#         # p=((x%10)*100)
#         # print(p)
#         # x=x-p