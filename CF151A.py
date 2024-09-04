n,k,l,c,d,p,nl,np=list(map(int,input().split()))
total_millilitre = k*l
total_slice = c*d
total_salt = p
z=[total_millilitre//nl,total_slice,total_salt//np]
z.sort()
print(z[0]//n)