operator = input("Enter an operator [+ - * /]: ")

if operator in ('+', '-', '*', '/'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operator == '+':
        result = num1 + num2
        print("Sum is " + str(result))
    elif operator == '-':
        result = num1 - num2
        print("Difference is " + str(result))
    elif operator == '*':
        result = num1 * num2
        print("Product is " + str(result))
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print("Division is " + str(result))
        else:
            print("Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter +, -, *, or /.")
