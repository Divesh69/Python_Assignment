#  Make a Python program that acts as a simple calculator. The program
#  should take two numbers and an operator (+, -, x, /) as input from the
#  user and perform the corresponding operation, displaying the result.
#  The program should also handle any value errors that may occur

print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option =int(input("choose an operation: "))
num1 =int(input("Enter first number:"))
num2 =int(input("Enter second number:"))
if(option == 1):
    result = num1 + num2
elif(option == 2):
    result = num1 - num2
elif(option == 3):
    result = num1 * num2
elif(option == 4):
    result = num1 / num2
else:
    print("Invalid")
print(f"The result of the operation is: {result}")