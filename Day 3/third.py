# Taking user input for two numbers
num1_str = input("Enter the first number: ")  # Asking the user to enter the first number as a string
num2_str = input("Enter the second number: ")  # Asking the user to enter the second number as a string

# Type casting input strings to integers
try:
    num1 = int(num1_str)  # Converting the first input to an integer
    num2 = int(num2_str)  # Converting the second input to an integer
except ValueError:
    print("Please enter valid numbers!")  # Handling error if input is not a number

# Performing arithmetic operations
sum_result = num1 + num2  # Adding the two numbers together
difference = num1 - num2  # Finding the difference between the two numbers
product = num1 * num2  # Multiplying the two numbers

# Constructing strings to display results
sum_str = f"The sum of {num1} and {num2} is: {sum_result}"  # Creating a string for the sum
diff_str = f"The difference between {num1} and {num2} is: {difference}"  # Creating a string for the difference
prod_str = f"The product of {num1} and {num2} is: {product}"  # Creating a string for the product

# Displaying the results
print(sum_str)  # Displaying the sum
print(diff_str)  # Displaying the difference
print(prod_str)  # Displaying the product
