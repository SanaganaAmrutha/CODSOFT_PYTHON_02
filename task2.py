print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice here (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "Division"
        else:
            result = "undefined (cannot divide by zero)"
            operation = "Division"
else:
    result = "Invalid input given"
    operation = "Invalid"

print(f"Operation: {operation}")
print(f"Result: {result}")
