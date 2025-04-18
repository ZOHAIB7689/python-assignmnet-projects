# The for loop iterates over a sequence (like a list, string, or range) and executes a block of code for each item for a specified or fixed number of times.

# Example Code:

# iterate over list 
fruits : list = ["apple","cherry","banana","mango"]
for fruit in fruits:
    print(fruit)

word : str = "Georgeopole"
for letter in word:
    print(letter)

# _____________________________________________________________________________________________________
# for Loop with else in Python
# In Python, a for loop can have an else block. The else block runs only if the loop completes without a break statement.

numbers = [1,2,3,4,5,6,7]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully")

# example 2 

for num in numbers:
    print(num)
    if num  == 3:
        print("breaking the loop")
        break
else:
    print("Loop completed successfully")  # this will not run

# example 3 Searching with else

for num in numbers:
    if num == 8:
        print("Number found")
        break
else:
    print("number not found!") # runs because 8 is not in the list


# ______________________________________________________________________________________________
# range in for loop 


# print numbers from 0 to 4
for i in range(5):
    print(i)


#print even numbers from 2 to 10
for i in range(2 , 11, 2):
    print(i)
    