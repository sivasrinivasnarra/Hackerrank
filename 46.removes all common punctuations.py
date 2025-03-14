import string
s=input("Enter a string:\n")
l=''.join([char for char in s if char not in  string.punctuation])
print(f"Output= {l}")