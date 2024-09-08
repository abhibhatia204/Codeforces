t = int(input())
for i in range (t):
    x = int(input())
    cnt = 0
    if x & (x-1)==0:
        cnt = 0
    else :
        cnt = 1
    if (cnt == 1):
        print("Yes")
    else:
        print("No")
        
        