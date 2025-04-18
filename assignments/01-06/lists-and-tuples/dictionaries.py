# A dictionary is a collection of key-value pairs that can be used to store and manage data in a structured way.

# The syntax for creating a dictionary is as follows:
# dictionary = {"key1":"value1","key2":"value2"......}

# Let's create a dictionary to represent a person:
person = {"name": "John", "age": 30, "city": "New York"}

# To access a specific element in the dictionary, we use its key. For example, to get the person's name:
print(person["name"])  # Output: John

# If we need to update a value in the dictionary, we can simply assign a new value to the existing key. For instance, let's update the person's age:
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding a new element to the dictionary is similar to updating an existing one. We just need to specify a new key and its corresponding value. Let's add the person's country:
person["country"] = "USA"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# If we want to remove an element from the dictionary, we use the del statement. For example, let's remove the 'city' key-value pair:
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Dictionaries provide several useful methods to work with their elements. Here are a few examples:

# 1. keys() - This method returns a view object that displays a list of all the keys available in the dictionary.
print(person.keys())  # Output: dict_keys(['name', 'age', 'country'])

# 2. values() - This method returns a view object that displays a list of all the values available in the dictionary.
print(person.values())  # Output: dict_values(['John', 31, 'USA'])

# 3. items() - This method returns a view object that displays a list of a dictionary’s key-value tuple pairs.
print(person.items())  # Output: dict_items([('name', 'John'), ('age', 31), ('country', 'USA')])

# 4. get() - This method returns the value of the item with the specified key. If the key does not exist, it returns a default value.
print(person.get("name"))  # Output: John
print(person.get("height", "Not available"))  # Output: Not available

# 5. update() - This method updates the dictionary with the specified key-value pairs.
person.update({"height": 180})
print(person)  # Output: {'name': 'John', 'age': 31, 'country': 'USA', 'height': 180}

# 6. pop() - This method removes the item with the specified key.
person.pop("age")
print(person)  # Output: {'name': 'John', 'country': 'USA', 'height': 180}

# 7. clear() - This method removes all the items from the dictionary.
person.clear()
print(person)  # Output: {}
