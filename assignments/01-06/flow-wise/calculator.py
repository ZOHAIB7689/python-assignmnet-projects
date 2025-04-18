operation: str  = input("Enter the operation (+, -,  *,/):")
num1: float = float(input("Enter the 1st number: "))
num2: float = float(input("Enter the 2nd number: "))


if operation == "+":
    result = num1 + num2 
elif operation == "-":
    result = num1 - num2
elif operation  == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1/num2
    else:
        result = "Error: Division by zero"
else :
    result = "Invalid operation"


print("Result: ", result)