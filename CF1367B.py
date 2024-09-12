t = int(input())
for i in range(t):
    v = int(input())
    odd = 0
    even = 0
    x = list(map(int,input().split()))
    for j in range(v):
        if x[j]%2!=j%2:
            if x[j]%2==0:
                even += 1
            else:
                odd += 1
    if even != odd:
        print(-1)
    else:
        print(even)