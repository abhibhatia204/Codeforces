n = int(input())
p = []
q = []
c = 0
for i in range(n):
    z = input()
    if len(p)==0:
        p.append(z)
    else:
        c = p[0]
        if z == c :
            p.append(z)
        else:
            q.append(z)
if len(p)>len(q):
    print(p[0])
else:
    print(q[0])