# creating a list 

fruits: list = ["apple", "banana","cherry"]
numbers: list = [10,20,30,40]
mixed : list = ["hello",42,3.14,True]


print(fruits, numbers, mixed)

# you can access list elements using indexing (starting from 0) and negative indexing

print(fruits[0]) # output apple
print(fruits[-2]) # output banana


# lists are mutable meaning their elements can be changed

fruits[-3] = " watermelon" #replacing the "apple" with "watermelon"
print(f"modified list{fruits}")


# list slicing

# Lists provide built in methods for efficient data manipulation
fruits.append("mango") #Adds a single element mango to the end
print(fruits) # Output:["watermelon","banana"......]

fruits.extend(["grape", "kiwi"]) # Adds  multiple elements
print(fruits) # Output : ['watermelon', 'banana', 'cherry','mango', 'grape','kiwi']


# Remove method
deleted = fruits.pop(1)
print(deleted) #Output :'cherry'
print(fruits) # Output: ['watermelon', 'mango', 'grape', 'kiwi']



# Sort a list 
#Ascending order
numbers: list[int] = [3,1,4,1,5,9]
numbers.sort()
print(numbers) #:[1,1,3,4,5,9]

# Descending Order

numbers.sort(reverse=True)
print(numbers) # :[9,5,4,3,1,1]
