z=input()
l = 0
cnt=0
while(cnt!=len(z)):
    for i in range(l, len(z)):
        if(len(z)-cnt >=3 and z[i]=="W" and z[i+1]=="U" and z[i+2]=="B"):
            l=i+3
            cnt+=3
            break
        else:
            print(z[i],end="")
            if(len(z)-cnt > 3 and  z[i+1]=="W" and z[i+2]=="U" and z[i+3]=="B"):
                print(" ", end="")
            cnt+= 1
    