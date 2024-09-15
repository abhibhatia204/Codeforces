t = int(input())
for i in range(t):
    n , m , q = list(map(int,input().split()))
    b1 , b2 = list(map(int,input().split()))
    c = min(b1,b2)
    d = max(b1,b2)
    a1 = int(input())
    if a1<b1 and a1<b2:
        print(abs(c-1))
    elif a1>b1 and a1>b2:
        print(abs(n-d))
    else:
        v = d-c-1
        if v%2==0:
            print((v//2))
        else:
            print((v+1)//2)
