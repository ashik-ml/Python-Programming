# Function Definitions
def greet(name):
    return f"Hello, {name}!"

def capitalize(text):
    return text.upper()

def greet_and_capitalize(name):
    greeting = greet(name)
    return capitalize(greeting)

# Call the functions
name = "Alice"
final_result = greet_and_capitalize(name)

# Display the results
print("Final Result:", final_result)

# Test cases with multiple lines of input
# Accept the count of test cases given in the 1st line
t = int(input())
# Run a loop to accept 't' inputs
for i in range(t):
    # Accept 2 integers on the 1st line of each test case
    A, B = map(int, input().split())
    # Accept 3 integers on the 2nd line of each test case
    C, D, E = map(int, input().split())
    # Output the 5 integers on a single line for each test case
    print(A, B, C, D, E)

# Test cases with multiple types of input
# Accept the count of test cases given in the 1st line
t = int(input())
# Run a loop to accept 't' test cases
for i in range(t):
    # Accept 2 integers on the 1st line of each test case
    A, B = map(int, input().split())     
    # Accept 1 string on the 2nd line of each test case
    C = input()
    # Output the 2 integers and 1 string on a single line for each test case
    print(A, B, C)
