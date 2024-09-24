#using variables
import sys
operation = input("choose the operation that you want to perfom (+,-,/,*)\n")
if operation not in['+','-','*','/']:
    print("Invalid Operation selected")
    sys.exit()
num1 = float(input("Enter the first number\n"))
num2 = float(input("enter the Second Number\n"))
result=None

if operation == '+':
    result = num1+num2
elif operation == '-':
   result = num1-num2
elif operation == '/':
   result = num1/num2
elif operation == '*':
    result = num1*num2

print("The result of 2 numbers is "+str(result))
