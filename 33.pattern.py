#Write a ‘Python’ program to Print the following Number pattern.

#1
#1 2 1
#1 2 3 2 1
#1 2 3 4 3 2 1
#1 2 3 4 5 4 3 2 1
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
        if j==i:
            for j in range (i-1,0,-1):
                print(j,end=" ")
    print()