t = int(input())
for i in range(t):
    z = input()
    c = int(z[0])-1
    x = c*10
    if len(z)==1:
        x += 1
    elif len(z)==2:
        x += 3
    elif len(z)==3:
        x += 6
    else:
        x += 10
    print(x)
    