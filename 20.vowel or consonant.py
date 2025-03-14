#Take an input character from the user and check whether the given input is vowel or consonant.
char=input("enter").lower()
v=['a','e','i','o','u']
if char in v:
    print("Vowel")
else:
    print("Consonant")