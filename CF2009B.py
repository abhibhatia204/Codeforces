t=int(input())
for i in range(t):
    r=int(input())
    z=[]
    for j in range(r):
        p=input()
        q= p.find("#")
        z.append(q+1)
    
    for m in range(len(z)-1,-1,-1):
        print(z[m],end=" ")