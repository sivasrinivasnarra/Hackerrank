s=input("Enter a string:\n")
l=list(s)
Sum=sum(int(char) for char in l if char.isdigit())
print(f"Sum={Sum}")
