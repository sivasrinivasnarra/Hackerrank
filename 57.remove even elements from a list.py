input_str = input("Input List:\n")
numbers = [int(x) for x in input_str.strip('[]').split(',')]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(f"List after removing all even numbers:  {odd_numbers}")