x = int(input())
c = bin(x)
ans = 0
for i in range(len(c)):
    if c[i]=="1":
        ans += 1
print(ans)