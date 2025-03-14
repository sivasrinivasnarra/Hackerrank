#Write a program to accept the name of a student and their marks in three subjects, each out of 100 and print the Result as Passed or Failed or Failed in Subject(s) based on a passing percentage of 40%.
n=str(input("Enter Name:\n"))
s1=int(input("Enter Subject1 marks:\n"))
s2=int(input("Enter Subject2 marks:\n"))
s3=int(input("Enter Subject3 marks:\n"))
if s1>40:
    if s2>40:
        if s3>40:
            print(f"Congratulation {n} you passed the exam")
        else:
            print(f"{n} you Failed in subject(s)")
    else:
        print(f"{n} you Failed in subject(s)")
else:
    if s2<40:
        if s3<40:
            print(f"{n} you Failed")
        else:
            print(f"{n} you Failed in subject(s)")
    else:
        print(f"{n} you Failed in subject(s)")