t = int(input())
for i in range(t):
    l = []
    z = input()
    # m = 0
    # cnt = 1
    # while cnt <= len(z):
    #     for j in range(m, len(z)):
    #         if j == 0 or j == len(z)-1:
    #             print(z[j], end="")
    #             cnt += 1
    #         else:
    #             print(z[j], end="")
    #             m = j +2
    #             cnt += 2
    #             break
    # print("")
                
    q = 1
    l.append(z[0])
    cnt = 0
    while(cnt<len(z)-2):
        for j in range(q,len(z)-1):
            if(z[j]==z[j+1]):
                l.append(z[j+1])
                q = j+2
                cnt += 2
                break
            else:
             l.append(z[j])
             cnt += 1
             break
    l.append(z[len(z)-1])
    for o in range(len(l)):
        print(l[o],end="")
    print("")