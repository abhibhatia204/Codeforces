t = int(input())
a = list(map(int,input().split()))
s = 0
d = 0
for i in range ((t//2)+1):
    if len(a)> 1:
        l = max(a[0],a[len(a)-1])
        s += l
        a.remove(l)
        v = max(a[0],a[len(a)-1])
        d += v
        a.remove(v)
    elif len(a) == 1:
        s += a[0]
    else:
        break
print(s,end=" ")
print(d)