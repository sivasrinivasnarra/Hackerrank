#Write a program to Print the following Number pattern.

#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
n=int(input("n"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
        if i==j:
            break
    print()