z=int(input())
y=list(map(int,input().split()))
ans=0
cnt=1
if(z==1):
    print("1")
else:    
    for i in range(z-1):
        if(y[i+1]>=y[i]):
            cnt+=1
        else:
            cnt=1
        if(cnt>ans):
            ans=cnt
    print(ans)