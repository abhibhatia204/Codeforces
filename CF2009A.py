t=int(input())
for i in range(t):
    x,y=list(map(int,input().split()))
    q=[]
    for j in range(x,y+1):
        c=j
        z=(c-x)+(y-c)
        q.append(z)
    q.sort()
    print(q[0])