n = int(input("n"))
k = []
l = []
for i in range(1, n+1):
    for j in range(1, i):
        if i % j == 0:
            k.append(j)
    if sum(k) == i:
        l.append(i)
        print(*l)
    k = []
    l=[]