n = int(input())
for l in range(n):
    y = int(input())
    s = y//2020
    for i in range(s+1):
        r = y- 2020 * i
        if r % 2021 == 0:
            print("YES")
            break
    else:
        print("NO")