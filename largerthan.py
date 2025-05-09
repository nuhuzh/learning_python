# Display two numbers in order of weight.

print("Please enter any two numbers...")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    print(f"Numbers in order: {second_number}, {first_number}... ")
else:
    print(f"Numbers in order: {first_number}, {second_number}... ")
