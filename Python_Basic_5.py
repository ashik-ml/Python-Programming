# While Loop
a = 0
while a < 7:
    print("The conter is :", a)
    a += 1

# While Loop with user input :

print("Insert a Number Please :")
num = int(input())
a = 0
while num > a:
    print(a)
    a += 1


# User Input Validation  :
password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted!")
    else:
        print("Incorrect password. Try again.")

# Summing Number  :
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print("Sum of numbers from 1 to 5:", total)

# Countdown :
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")


