# Get input from the user
number = int(input("Enter a number: "))

# Print multiplication table up to 10
print(f"\nMultiplication Table for {number}:\n")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
