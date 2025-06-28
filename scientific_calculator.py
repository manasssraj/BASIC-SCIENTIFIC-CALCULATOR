import math

def calculator():
    print("Basic Scientific Calculator")
    print("Available operations:")
    print(" +, -, *, /, %, pow, sqrt, sin, cos, tan, log, ln, exp, fact")
    print("Use 'exit' to quit.")

    while True:
        operation = input("\nEnter operation: ").strip().lower()

        if operation == "exit":
            break
        elif operation in ['+', '-', '*', '/', '%', 'pow']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if operation == '+':
                print("Result:", a + b)
            elif operation == '-':
                print("Result:", a - b)
            elif operation == '*':
                print("Result:", a * b)
            elif operation == '/':
                print("Result:", a / b if b != 0 else "Error: Division by zero")
            elif operation == '%':
                print("Result:", a % b)
            elif operation == 'pow':
                print("Result:", math.pow(a, b))

        elif operation == 'sqrt':
            a = float(input("Enter number: "))
            print("Result:", math.sqrt(a))

        elif operation in ['sin', 'cos', 'tan']:
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)
            if operation == 'sin':
                print("Result:", math.sin(radians))
            elif operation == 'cos':
                print("Result:", math.cos(radians))
            elif operation == 'tan':
                print("Result:", math.tan(radians))

        elif operation == 'log':
            a = float(input("Enter number: "))
            print("Result:", math.log10(a))
        elif operation == 'ln':
            a = float(input("Enter number: "))
            print("Result:", math.log(a))
        elif operation == 'exp':
            a = float(input("Enter power: "))
            print("Result:", math.exp(a))
        elif operation == 'fact':
            a = int(input("Enter integer: "))
            print("Result:", math.factorial(a))
        else:
            print("Invalid operation.")

calculator()
