n , m = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
ans = 0
cnt = 0
for i in range(m):
    if a[i]<0:
        ans += abs(a[i])
    # else :
    #     ans -= a[i]
print(ans)