t = int(input())
for i in range(t):
    a , b , c = list(map(int,input().split()))
    if a==b:
        print(c)
    elif b==c:
        print(a)
    else:
        print(b)