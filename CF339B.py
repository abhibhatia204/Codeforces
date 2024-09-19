n , m = list(map(int,input().split()))
y = []
x = list(map(int,input().split()))
y.append(x)
ans = 0
a = 1
for i in range(len(y[0])):
    if y[0][i] >= a :
        ans += y[0][i]-a
        a = y[0][i]
    else:
        ans += n-a+y[0][i]
        a = y[0][i]
print(ans)
    