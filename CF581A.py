ab = list(map(int,input().split()))
if(ab[0]==ab[1]):
    print(ab[0],end=" ")
    print("0")
elif(ab[0]>ab[1]):
    print(ab[1],end=" ")
    c=ab[0]-ab[1]
    print(c//2)
else:
    print(ab[0],end=" ")
    v=ab[1]-ab[0]
    print(v//2)
    