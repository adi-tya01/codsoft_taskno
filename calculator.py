# Simple Calculator in Python

def calculator():
    print("===== SIMPLE CALCULATOR =====")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: Division by zero is not allowed!")
        else:
            print("\nInvalid choice. Please select 1-4.")
    
    except ValueError:
        print("\nError: Please enter valid numbers.")

# Run the calculator
calculator()