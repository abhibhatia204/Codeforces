t = int(input())
x = "codeforces"
for i in range (t):
    z = input()
    cnt = 0
    for j in range(len(x)):
        if(z==x[j]):
            cnt = 1
            break
    if cnt == 1:
        print("YES")
    else:
        print("NO")
