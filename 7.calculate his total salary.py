#Rahul’s basic salary is input through the keyboard. His dearness allowance is 50% of basic salary and house rent allowance is 30% of basic salary. Write a program to calculate his total salary.
b=int(input("Enter Basic salary:\n" ))
DA=b/2
HRA=0.3*b
print(f"DA: {DA:.2f} \nHRA: {HRA:.2f} \nTotal salary: {(b+DA+HRA):.2f}")