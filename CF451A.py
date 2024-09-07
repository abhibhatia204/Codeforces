a , b = list(map(int,input().split()))
cnt = -1
for i in range (0,max(a,b)):
    a -= 1
    b -= 1
    cnt += 1
    if a==0 or b==0:
        break
if (cnt%2==0):
    print("Akshat")
else:
    print("Malvika")