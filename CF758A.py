t = int(input())
x = list(map(int,input().split()))
c = max(x)
ans = 0
for i in range(t):
    v = c-x[i]
    ans += v
print(ans)