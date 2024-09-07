t = int(input())
for i in range(t):
    z = input()
    x = [int(z[0]), int(z[1]),int(z[2])]
    y = [int(z[3]), int(z[4]),int(z[5])]
    if(sum(x)==sum(y)):
        print("YES")
    else:
        print("NO")