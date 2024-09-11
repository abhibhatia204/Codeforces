n = int(input())
if n>0:
    print(n)
else:
    z = str(n)
    a = z[:len(z)-1]
    b = z[:len(z)-2]+z[len(z)-1:]
    x = max(int(a),int(b))
    print(x)
