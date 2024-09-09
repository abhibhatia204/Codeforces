import math
def pn(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return True
    return False           
t = int(input())
f = 0
for i in range(0,t+1):
    for j in range(t+1,-1,-1):
        if i+j==t and pn(i) and pn(j):
            f +=1 
            break
    if f > 0:
        print(i, j)
        break