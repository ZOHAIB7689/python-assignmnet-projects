# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.


my_set : set = {123,452,5,6,}
my_set2 :set = set([123,452,5,6])
print("my set             =", my_set)                      #my_set            =  {123, 452, 5, 6}
print("my set2             =", my_set2)                 #my_set2            =  {123, 452, 5, 6}
print("type(myset)          =",type(my_set))        #<class 'set'>
print("type(myset2)          =",type(my_set2))    #<class 'set'>
print("my_set == myset2", my_set == my_set2)  # = True

# A set can store only immutable objects such as number (int, float, complex or bool), string or tuple. If you try to put a list or a dictionary in the set collection, Python raises a TypeError.

# my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
# print(my_set)

# it can hold multiple datatypes at once
multi_type_set : set = {7, 9.0 ,False,True ,"Hello! World", (1,5,9,'hi')}
print(multi_type_set)  #{False, True, 7, 9.0, 'Hello! World', (1, 5, 9, 'hi')}


# Unordered
set3 :set = {'Java', 'Python','Javascript','Java'}
print(set3) #everytime on runtime it will give different ordered output

# Unchangeable

new_set: set = {1,2,3,4,5}
print(my_set)  # Output: {1, 2, 3, 4, 5}


# try to change any item it wil raise an error
try:
    new_set[0] = 10   # Sets are unordered so indexing doesn't work
except TypeError as e:
    print(e)  #'set' object does not support item assignment
# programme execution continues as normal if you handle the error like this


my_new_set: set = {1,2,3,4,5,'A','a'}
print(my_new_set)  # Output{1, 2, 3, 4, 5, 'a', 'A'}
# Remove an item
my_new_set.remove(3) 
my_new_set.remove('A')
print(my_new_set)   # Output{1, 2, 4, 5, 'a'}

my_new_set.add(6)
print(my_new_set) # Output {1, 2, 4, 5, 6, 'a'}

#Use difference_update() method to remove multiple element at once
my_new_set.difference_update({1,5,3,'A'})
print(my_new_set) # Output {2, 4, 6, 'a'}

my_new_set.update([7,8,9,"Hello"])
print(my_new_set) #Output  {2, 4, 'Hello', 6, 7, 8, 9, 'a'}

# _____________________________________________________________________________________________________________________________________________________________


# Using the union() method or | operator:

#Union
uni_set:set =  {1,2,3,5}
uni_set_2:set =  {1,5,6,7,}

uni_set_3 = uni_set.union(uni_set_2)
print(uni_set_3)

# | operator
uni_set_4 = uni_set | uni_set_2