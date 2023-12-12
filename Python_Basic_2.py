# Take input on python
# Get input from the user
print("Get Input From The User ................")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_phone = input("Enter your phone number : ")
user_address = input("Enter your your address : ")

# Display the input data
print("Name:", user_name)
print("Age:", user_age)
print("Phone:", user_phone)
print("Your Address is :", user_address)

# IF Statement
print("IF Statement using  operators used in Python conditions ...................")
age = 25
vage = 18

if age >= vage:
    print("Old enough to vote!")
else:
    print("Not old enough to vote.")

# Learning About Indentation Error.
# Need Space after if and else statement.
print("Learning About Indentation Error .............")
r = 1000
w = 3222
if r > w:
    # This code will not run due to improper indentation
    print("White balls are out of stock")
else:
    # Fix the error by putting a space before both print
    print("Your order is Confirmed")

# Update the blanks in the code below to solve the problem
print("Code chef problem soled.....................")
r = 24
k = 32

if r > k:
    print("Ram is heavier than Karan")
elif r < k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")

r = 78
k = 78

if r > k:
    print("Ram is heavier than Karan")
elif r < k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")


