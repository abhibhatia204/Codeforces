a1, a2, a3, a4 = list(map(int,input().split()))
z = input()
ans = 0
for i in range(len(z)):
    if z[i]=="1":
        ans += a1
    elif z[i]=="2":
        ans += a2
    elif z[i]=="3":
        ans += a3
    else:
        ans += a4
print(ans)