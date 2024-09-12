t = int(input())
for i in range(t):
    c = int(input())
    b = list(map(int,input().split()))
    x = max(b)
    z = min(b)
    print(x-z)