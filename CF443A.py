z=input()
y=[]
for i in range(1,len(z)-1,3):
    y.append(z[i])
p=set(y)
print(len(p))
