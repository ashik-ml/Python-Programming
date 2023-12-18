# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Calculate the sum of numbers from 1 to 5
sum_result = 0
for i in range(1, 6):
    sum_result += i
print("Sum:", sum_result)

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

# Calculate the product of numbers from 1 to 5
product_result = 1
for i in range(1, 6):
    product_result *= i
print("Product:", product_result)

# Example 5: Print squares of numbers from 1 to 5
for i in range(1, 6):
    print(f"Square of {i}: {i*i}")

# Count the number of digits in a given number
number = 12345
digit_count = 0
for digit in str(number):
    digit_count += 1
print(f"Number of digits in {number}: {digit_count}")

# Print a multiplication table for a given number (e.g., 7)
multiplication_number = 7
for i in range(1, 11):
    print(f"{multiplication_number} x {i} = {multiplication_number*i}")

# Calculate the factorial of a number (e.g., 5!)
factorial_number = 5
factorial_result = 1
for i in range(1, factorial_number + 1):
    factorial_result *= i
print(f"{factorial_number}! = {factorial_result}")

# Print a pattern of stars (right-angled triangle)
for i in range(1, 6):
    print('*' * i)

# Reverse a list
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in reversed(original_list):
    reversed_list.append(item)
print("Original List:", original_list)
print("Reversed List:", reversed_list)
