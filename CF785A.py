z=int(input())
cnt=0
for i in range(z):
    a=input()
    if(a=="Tetrahedron"):
        cnt+=4
    elif(a=="Cube"):
        cnt+=6
    
    elif(a=="Octahedron"):
        cnt+=8
    
    elif(a=="Dodecahedron"):
        cnt+=12
    
    else:
        cnt+=20
print(cnt)
    