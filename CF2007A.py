t = int(input())
for i in range (t):
    l , r = list(map(int,input().split()))
    o = []
    for i in range(l,r+1):
        if i%2!=0:
            o.append(i)
    print(len(o)//2)
