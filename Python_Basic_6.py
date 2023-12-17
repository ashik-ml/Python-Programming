def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    print(square)
    print(cube)

# Using the function for numbers 2, 3, and 4
calculate_square_and_cube(2)
calculate_square_and_cube(3)
calculate_square_and_cube(4)


# Function with parameters and return value
def add_numbers(a, b):
    return a + b

# Function with a default parameter
def power(base, exponent=2):
    return base ** exponent

# Function with a docstring
def square(num):
    """
    This function returns the square of a number.
    """
    return num ** 2

# Recursive function
def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

# Lambda function
square_lambda = lambda x: x ** 2

# Function with variable number of arguments
def average(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

# Function with keyword arguments
def person_info(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

# Function with a global variable
global_variable = 10
def add_global(num):
    global global_variable
    global_variable += num
    return global_variable

# Example usage
print(greet())
print(add_numbers(3, 4))
print(power(3, 4))
print(square(5))
print(factorial(5))
print(square_lambda(5))
print(average(2, 4, 6, 8))
print(person_info(name="John", age=25, city="New York"))
print(add_global(5))






