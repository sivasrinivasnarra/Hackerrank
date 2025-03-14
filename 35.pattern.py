#Write a program to print Full Triangle Pyramid pattern using an asterisk.

 #       *
  #     * *
   #   * * *
    # * * * *
    #* * * * *
   #* * * * * *
  #* * * * * * *
n=int(input())
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()