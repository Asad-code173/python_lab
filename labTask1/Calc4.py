#Using Set
numbers = set()
for i in range(5):
    num = input(f"Enter numbers {i+1} ")
    if num:
        numbers.add(float(num))
    else:
        break
result = 0

if len(numbers) < 5:
    print("Some duplicates were removed.")

operation = input("Choose operation: +, -, *, /: ")
numbers = list(numbers)
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
