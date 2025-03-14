n1 = int(input("Enter 1st number\n"))
n2 = int(input("Enter 2nd number\n"))
n3 = int(input("Enter 3rd number\n"))

if n1 > n2:
    if n1 > n3:
        print(f"Largest number among {n1},{n2} and {n3} is {n1}")
    else:
        print(f"Largest number among {n1},{n2} and {n3} is {n3}")
else:
    if n2 > n3:
        print(f"Largest number among {n1},{n2} and {n3} is {n2}")
    else:
        print(f"Largest number among {n1},{n2} and {n3} is {n3}")