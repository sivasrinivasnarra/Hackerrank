s1 = input("Enter a string:\n").strip()  # .strip() removes any leading/trailing whitespace

if len(s1) <= 1:
    print(f"{s1} is not a palindrome")
else:
    l = list(s1.lower())
    k = l[::-1]
    c = "".join(k)

    if s1.lower() == c:
        print(f"{s1} is palindrome")
    else:
        print(f"{s1} is not palindrome")