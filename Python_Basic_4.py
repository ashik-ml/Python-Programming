# Creating Arrays

# Update the 3rd month in the list below to "Mar"
months = ["Jan", "Feb", "Dec", "Apr"]
months[2] = "Mar"
print(months)

# Output the 3rd element of the following array to the console
num = [1, 2, 3, 4, 5]
print(num[2])

# Displaying the count of elements
Numbers = [10, 20, 30, 40, 50, 60]
print(len(Numbers))

# Creating a list of fruits
fruits = ["apple", "banana", "orange", "grape"]

# Accessing elements
print("First fruit:", fruits[0])  # Output: apple

# Modifying elements
fruits[1] = "kiwi"
print("Modified list:", fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape']

# Adding elements
fruits.append("mango")
print("List after adding mango:", fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape', 'mango']

# Removing elements
removed_fruit = fruits.pop(2)
print("List after removing orange:", fruits)  # Output: ['apple', 'kiwi', 'grape', 'mango']
print("Removed fruit:", removed_fruit)  # Output: orange

# Finding the length of the list
num_of_fruits = len(fruits)
print("Number of fruits:", num_of_fruits)  # Output: 4

# Checking for existence
is_apple_present = "apple" in fruits
print("Is 'apple' present?", is_apple_present)  # Output: True

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)  # Output: ['apple', 'grape', 'kiwi', 'mango']

