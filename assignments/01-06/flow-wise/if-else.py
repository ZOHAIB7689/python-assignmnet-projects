# The if statement is used to execute a block of code only if condition is true
num: int = 10
if num >0 :
    print("The number is positive")

# The else statement is used to execute a block of code if the function is false

num1 : int = -5
if num1>0:
    print("the number is positve ")
else:
    print("The number is negative")



# the elif statement is used to check multiple conditions it stands for else if

num3:int = 0
if num3 >0:
    print("the number is positive")
elif num3 < 0:
    print("the number is negative")
else:
    print("the number is zero")

# _________________________________________________________________________________________________________
age= 25
is_student: bool = True



# and (True if both conditions are True) 
if age > 18 and is_student:
    print("You are eligible for a student discount")

# or (True if atleast one condition is true)
if age< 12 or age> 60:
    print("You qualify for a special dixcount")

# not( reverse the result of a condition)
if not is_student:
    print("You are not a student")

# __________________________________________________________________________________________________________________

# nested if statements
# statements can be nested inside other if statements to check multiple conditions

number: int = 10 
if num > 0:
    if num % 2 ==0:
        print("print the number is positive and even") 
    else:
        print("the number is positive and odd")
else:
    print("the numbe is negative")


# practical example
