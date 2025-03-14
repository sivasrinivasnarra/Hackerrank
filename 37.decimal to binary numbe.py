n=int(input("n"))
p=[]
while n//2 >=1:

    p.append(n%2)
    n=n//2

p.append(1)
p1=p[::-1]
p2=''.join(map(str,p1))
print(p2)