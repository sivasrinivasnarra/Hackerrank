l=input("Enter list:\n")
n=int(input("Enter an integer:\n"))
k = l.strip("[]").replace("'", "").split(", ")
m=[]
for word in k:
    if len(word)>n:
        m.append(word)

print(f"Output= {m}")