t = int(input())
for i in range(t):
    x , y , n = list(map(int,input().split()))
    c = n
    while True:
        if(c-(n//x)*x>=y):
            print((n//x)*x+y)
            break
        else:
            n -= x