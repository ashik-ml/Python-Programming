# Comparing two numbers
print("Comparing Two Numbers......")
num_1 = 15
num_2 = 25

if num_1 > num_2:
    print("Number 1 is greater than Number 2.")
elif num_1 < num_2:
    print("Number 1 is less than Number 2.")
else:
    print("Number 1 is equal to Number 2.")



# Checking if a number is positive or negative
print("Checking if a number is positive or negative......")
num = -8

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Checking divisibility by 3 and 5
print("Checking divisibility by 3 and 5......")
number = 30

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 3 or 5.")



# Determining if a number is a prime number
print("Determining if a number is a prime number......")
num_prime = 13

if num_prime > 1:
    for i in range(2, int(num_prime**0.5) + 1):
        if num_prime % i == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number.")



# Categorizing a number as odd or even
print("Categorizing a number as odd or even......")
number_cat = 42

if number_cat % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



# Checking if a number is within a specific range
print("Checking if a number is within a specific range......")
num_range = 75

if 50 <= num_range <= 100:
    print("The number is within the range of 50 to 100.")
else:
    print("The number is outside the range of 50 to 100.")



# Checking the length of the name
print("Checking the length of the name......")

my_name = "Tahmina"

if len(my_name) > 5:
    print("The name is long.")
else:
    print("The name is short.")



# Greeting a specific person
print("Greeting a specific person......")

my_name = "Sohel"

if my_name.lower() == "sohel":
    print("Hello, Sohel!")
else:
    print("You're not Sohel.")



# Checking for the letter 'n' in the name
print("Checking for the letter 'n' in the name......")
my_name = "Nasrin"

if "n" in my_name.lower():
    print("The name contains the letter 'n'.")
else:
    print("The name does not contain the letter 'n'.")



# Determining if the name has an even or odd number of characters
print(" Determining if the name has an even or odd number of characters......")

my_name = "Farida"

if len(my_name) % 2 == 0:
    print("The name has an even number of characters.")
else:
    print("The name has an odd number of characters.")



# Checking if the name starts with the letter 'R'
print(" Checking if the name starts with the letter 'R'......")
my_name = "Rahim"

if my_name.startswith("R"):
    print("The name starts with the letter 'R'.")
else:
    print("The name does not start with the letter 'R'.") 
