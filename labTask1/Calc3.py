import sys

history = {}
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation that you want to perform (+, -, *, /): ")
if operation not in ['+', '-', '*', '/']:
    print("Invalid Operation selected")
    sys.exit()
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
history[operation] = result

print(f"The result of {num1} {operation} {num2} is {result}")



print("Operation History:")
for op, res in history.items():
    print(f"{op}: {res}")

