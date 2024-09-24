#Using List
numbers = []
for i in range(5):
    num = input(f"Enter number {i+1} ")
    if num:
        numbers.append(float(num))
    else:
        break

#
operation = input("Choose operation: +, -, *, /: ")
result = 0

if operation == '+':
    for num in numbers:
        result+=num
elif operation == '-':
    result = numbers[0]
    for num in numbers[1:]:
     result-=num
elif operation == '*':
    result=1
    for num in numbers:
        result *= num
elif operation == '/':
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            result = "Error! Division by zero."
            break
else:
    result = "Invalid operation."
print("Result:", result)
