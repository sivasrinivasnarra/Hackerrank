s=input("Enter List:\n")
l=s.strip('[]').split(',')
k=list(l)
k=[int(x) for x in k]
m=k[0]
k[0]=k[-1]
k[-1]=m
print(f"New list is: {k}")