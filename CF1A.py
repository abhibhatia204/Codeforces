n , m , a = list(map(int,input().split()))
ar = n * m
asq = a * a
if asq >= ar :
    print("1")
elif n <=a and m > a:   
    c = m//a
    if m % a != 0:
        print(c+1)
    else:
        print(c)
elif n > a and m <= a: 
    d = n//a
    if n % a != 0:
        print(d+1)
    else:
        print(d)
else:
    q = n//a
    w = m//a
    if n%a!=0:
        q +=1
    if m%a!=0:
        w += 1
    print(q*w)