#Write a Program to accept Marks of 3 Subjects and Display the Grade

#If the percentage is greater than 70, “Grade: A” is printed.
#If the percentage is in between 60 and 70, “Grade: B” is printed.
#If the percentage is in between 50 and 60, “Grade: C” is printed.
#If the percentage is in between 40 and 50, “Grade: D” is printed.
#If the percentage is below 40, “Grade: F” is printed.
s1 = int(input("Enter Subject1 marks:\n"))
s2 = int(input("Enter Subject2 marks:\n"))
s3 = int(input("Enter Subject3 marks:\n"))
p = (s1 + s2 + s3) * 100 / 300
if p < 40:
    print("Grade F")
else:
    if p < 50:
        print("Grade D")
    else:
        if p < 60:
            print("Grade C")
        else:
            if p < 70:
                print("Grade B")
            else:
                print("Grade A")
