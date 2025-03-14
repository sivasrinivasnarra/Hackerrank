s=input("Enter List of Elements:\n")
k=[int(x) for x in s.strip('[]').split(',')]
l=sorted(k,reverse=True)
print(f"Second largest element is: {l[1]}")