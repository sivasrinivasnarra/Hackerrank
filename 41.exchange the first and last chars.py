s=input("Enter a string:\n")
l=list(s)
if len(l)>1:
    l[0],l[-1]=l[-1],l[0]
k="".join(l)

print(f"Output= {k}")