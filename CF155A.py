t=int(input())
k=list(map(int,input().split()))
a=0
b=0
if(t>1):
    if(k[0]<k[1]):
        a=k[0]
        b=k[1]
    else:
        a=k[1]
        b=k[0]
    cnt=1
    for i in range(2,t):
        if(k[i]>=a and k[i]<=b):
            continue
        elif(k[i]>b):
            b=k[i]
            cnt+=1
        else:
            a=k[i]
            cnt+=1
else:
    cnt=0
if t > 1 and k[0] ==  k[1]:
    print(cnt-1)
else:
    print(cnt)