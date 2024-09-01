z=int(input())
for i in range(z):
    a,b=list(map(int,input().split()))
    if(a==0 and b%2!=0 or b==0 and a%2!=0):
        print("NO")
    elif(a%2==0 and b==0 or a==0 and b%2==0):
        print("YES")
    elif(a%2==0 and b%2==0):
        print("YES")
    elif(a%2!=0 and b%2!=0):
        print("NO")
    elif(a%2==0 and b%2!=0):
        print("YES")
    else:
        print("NO")