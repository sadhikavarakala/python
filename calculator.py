print("welcome to calculator")

while True:
    num1 = float(input("Enter first number:"))
    operator = input("Enter operator (+, -, *, /):")
    num2 = float(input("Enter second number:"))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed." )
            continue
    else:
        print("Error: Invalid operator.")
        continue

    print("result:", result)

    choice = input("Do you want to calculate again? (yes/no): ")
    if choice.lower() != 'yes':
        print("Thank you for using the calculator!")
        break
    