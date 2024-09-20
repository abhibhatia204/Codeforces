import math
t = int(input())
for i in range(t):
    n = int(input())
    x , y = list(map(int,input().split()))
    c = min(x,y)
    ans = math.ceil(n/c)
    print(ans)