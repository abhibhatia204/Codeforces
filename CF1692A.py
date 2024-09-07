t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    cn=0
    for i in range(1,4):
        if(a[i]>a[0]):
            cn+=1
    print(cn)