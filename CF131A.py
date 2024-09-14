x = input()
cnt = 0
cnt1 = 0
v = x[1:]
if x[0].isupper():
    for i in range(1,len(x)):
        if x[i].isupper():
            cnt += 1
    if len(v)==cnt :
        print(x.lower())
    else :
        print(x)
else:
    for i in range(1,len(x)):    
        if x[i].isupper():
            cnt1 += 1
    if(cnt1==len(v)):
        print(x[0].upper()+x[1:].lower())
    else:
        print(x)   
