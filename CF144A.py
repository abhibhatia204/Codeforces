n = int(input())
a = list(map(int, input().split()))
lar = 0
sam = 0
for i in range(n):
    if a[i] == min(a):
        sam = i+1  
for i in range(n-1, -1, -1):
    if a[i] == max(a):
        lar = i+1  
if lar > sam:
    print((lar-1) + (n - sam) -1)
else:
    print((lar-1) + (n - sam))