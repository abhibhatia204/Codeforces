n=int(input())
y=[]
cnt=0
for i in range(n):
    a=list(map(int,input().split()))
    y.append(a)
for i in range(n):
    for j in range(n):
        if y[i][0] == y[j][1]:
            cnt+=1
print(cnt)
    
    