n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
b=10000000
cnt = 0
for i in range(0,k-n+1):
    cnt = a[i+n-1] - a[i]
    b=min(b , cnt)
print(b)