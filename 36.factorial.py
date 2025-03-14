n=int(input("Enter any number:\n"))
p=1
for i in range(n,0,-1):
    p=i*p
print(f"Factorial of {n} is {p}")
