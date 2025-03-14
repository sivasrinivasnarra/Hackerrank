#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
n= int(input("Enter a number:\n"))
if n%2==0:
    print("You picked an even number")
else:
    print("You picked an odd number")