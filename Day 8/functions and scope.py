# Global variable
global_var = 100

def greet(name):
    """This function prints a greeting."""
    print(f"Hello, {name}!")

def power(base, exponent=2):
    """Calculate the power of a number."""
    result = base ** exponent
    return result

def my_function():
    local_var = 5
    print(f"Local variable: {local_var}")
    print(f"Global variable: {global_var}")

# Call the functions
greet("vasay bhaii")
greet("izhan bhaii")
greet("elvish bhaii")
result1 = power(3)        # Uses default exponent (2)
result2 = power(3, 3)     # Specify both base and exponent

my_function()

# Print the results
print("Power result (default exponent):", result1)
print("Power result (custom exponent):", result2)
