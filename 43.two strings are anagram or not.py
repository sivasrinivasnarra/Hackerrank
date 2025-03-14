s1 = input("Enter strings\n")
s2 = input()

# Remove spaces and convert to lowercase
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Check if sorted versions are the same
if sorted(s1) == sorted(s2):
    print("Strings are anagram")
else:
    print("Strings are Not anagram")
