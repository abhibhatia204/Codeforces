t,k=list(map(int,input().split()))
cnt=1
c=0
ans = 0
while(ans == 0):
    v=cnt*t
    c=v%10
    if(c==0) or (c == k):
        ans = cnt
    cnt += 1
print(ans)