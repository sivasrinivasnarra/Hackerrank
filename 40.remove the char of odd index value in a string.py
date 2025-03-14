s=input("Enter the string:\n")
k="".join(s[i] for i in range(len(s)) if i%2==0 )
print(f"Output= {k}")