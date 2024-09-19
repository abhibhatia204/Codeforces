s , n = list(map(int,input().split()))
cnt = 0
z =[]
for i in range(n):
    xy = list(map(int,input().split()))
    z.append(xy)
z.sort()
for k in range (len(z)):
    if z[k][0] < s:
        cnt += 1
        s = s + z[k][1]
        
if cnt == n:
    print("YES")
else:
    print("NO")     