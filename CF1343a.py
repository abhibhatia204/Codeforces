t = int(input())
for i in range(t):
    z = int(input())
    k = 1
    while True :
        deno = 2**k-1
        if deno > z:
            break
        if z % deno == 0:
            x = z//deno
            if x!= z :
                print(x)
                break
        k+=1