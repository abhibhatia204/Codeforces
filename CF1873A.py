t = int(input())
for i in range(t):
    z = input()
    if z[0]=="a" or z[1] == "b" or z[2] == "c":
        print("YES")
    # elif z[1]=='a' and z[2]=="c":
    #     print("YES")
    # elif z[2]=="a" and z[0]=="c":
    #     print("YES")
    else:
        print("NO")