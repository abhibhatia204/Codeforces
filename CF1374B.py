t = int(input())
for i in range(0,t):
    n = int(input())
    twos = 0
    threes = 0
    while(n%2==0):
        n = n/2
        twos+=1
    while(n%3==0):
        n = n/3
        threes+=1
    if(n!=1):
        print("-1")
    else:
        if(twos>threes):
            print("-1")
        else:
            print((threes-twos)+threes)
 
 
 
 
