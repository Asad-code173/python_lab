#using a tuple
import sys
num1 = float(input("Enter the First Number\n"))
num2 = float(input("Enter the Second Number\n"))
numbers = (num1,num2)
print(numbers)
operation = input("choose the operation that you want to perfom (+,-,/,*)\n")
if operation not in['+','-','*','/']:
    print("Invalid Operation selected")
    sys.exit()
if operation == '+':
    result = numbers[0]+numbers[1]
elif operation == '-':
   result = numbers[0]-numbers[1]
elif operation == '/':
   result = numbers[0]/numbers[1]
elif operation == '*':
    result = numbers[0]*numbers[1]

print("The result of 2 numbers is "+str(result))

