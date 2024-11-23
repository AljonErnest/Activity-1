def calculator(arth=None):
        print("Calculator")
        print("Select Arithmetic Operations:")
        print("A for Add (+)")
        print("S for Subtract (-)")
        print("M for Multiply (x)")
        print("D for Division (/)")

        while True:
            choice = input("Enter choice (A/S/M/D): ")
            choice = choice.upper()
            if choice in ['A', 'S', 'M', 'D']:
                break
            else:
                print("Invalid Input Please Try Again")

        while True:
            try:
                num1 = int(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                num2 = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

        while True:
            try:
                if choice == 'A':
                    print(f"Result: {num1 + num2}")
                    break
                elif choice == 'S':
                    print(f"Result: {num1 - num2}")
                    break
                elif choice == 'M':
                    print(f"Result: {num1 * num2}")
                    break
                elif choice == 'D':
                    if num2 != 0:
                        print(f"Result: {num1 / num2}")
                        break
                    else:
                        print("Error: The Output would be Undefined")
            except ValueError:
                print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()