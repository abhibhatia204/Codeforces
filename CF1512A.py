t=int(input())
for i in range(t):
    v = int(input())
    ans = 0
    a = list(map(int,input().split()))
    b = list(set(a))
    cnt = 0
    cnt1 = 0
    for j in range(3):
        if a[j] == b[0]:
            cnt += 1
        else:
            cnt1 += 1
    # z = b[min(cnt,cnt1)]
    if cnt <= 1:
        z = b[0]
    else:
        z = b[1]
    for j in range(v):
        if(a[j] == z):
            print(j+1) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for j in range(1,v+1):
    #     if(a[j]!=a[j+1]):
    #         ans=j+2
    #         break
    #     else:
    #         continue
      
            
            