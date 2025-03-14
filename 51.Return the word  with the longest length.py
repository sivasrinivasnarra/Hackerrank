s = input("Enter List of Words \n")
l = s.strip('[]').split(',')
max = 0
longest = ""  # Initialize the variable to store the longest word

for word in l:
    word = word.strip().strip("'\"")  # Remove any leading or trailing whitespace
    if len(word) > max:
        max = len(word)
        longest = word

print(f"The word with the longest length is: {longest}")