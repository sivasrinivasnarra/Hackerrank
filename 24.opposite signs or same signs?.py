n1=int(input("Enter the value of a\n"))
n2=int(input("Enter the value of b\n"))
p=n1*n2
if p>0:
    print("Integer have the same sign")
else:
    if p==0:
        print("zero")
    else:
        print("Integers have the opposite sign")