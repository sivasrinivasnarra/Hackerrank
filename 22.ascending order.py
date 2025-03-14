#Write a Program to accept three numbers from user and print it in ascending order.
n1=int(input("Enter First number:\n"))
n2=int(input("Enter Second number:\n"))
n3=int(input("Enter Third number:\n"))
if n1<n2:
    if n1<n3:
        if n2<n3:
            print(f"Numbers in Ascending order:  {n1} {n2} {n3}")
        else:
            print(f"Numbers in Ascending order:  {n1} {n3} {n2}")
    else:
        print(f"Numbers in Ascending order:  {n3} {n1} {n2}")
else:
    if n2<n3:
        if n1<n3:
              print(f"Numbers in Ascending order:  {n2} {n1} {n3}")
        else:
              print(f"Numbers in Ascending order:  {n2} {n3} {n1}")
    else:
         print(f"Numbers in Ascending order:  {n3} {n2} {n1}")