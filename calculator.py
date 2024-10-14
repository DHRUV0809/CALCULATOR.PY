def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select operation: 1. Addition (+) 2. Subtraction (-) 3. Multiplication (*) 4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid choice.")

calculator()