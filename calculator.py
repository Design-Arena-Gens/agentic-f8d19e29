#!/usr/bin/env python3
"""
Calculator Application
A simple command-line calculator that performs basic arithmetic operations
"""

def add(x, y):
    """Addition operation"""
    return x + y

def subtract(x, y):
    """Subtraction operation"""
    return x - y

def multiply(x, y):
    """Multiplication operation"""
    return x * y

def divide(x, y):
    """Division operation"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """Main calculator function"""
    print("=" * 50)
    print("SIMPLE CALCULATOR")
    print("=" * 50)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")

            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    calculator()
