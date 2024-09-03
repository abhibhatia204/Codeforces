x=int(input())
n=list(map(int,input().split()))
p=0
ans=0
for i in range(x):
    if n[i]<0:
        if p==0:
            ans+=n[i]
        else:
            p += n[i]
    else :
        p += n[i]
print (ans*-1)
    
    