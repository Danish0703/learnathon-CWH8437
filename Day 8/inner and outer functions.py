
def outer_function():
    x = 5  # Variable in the outer function's scope
    
    def inner_function():
        y = 3  # Variable in the inner function's scope
        return x + y  # Accessing x from the outer function's scope
    
    result = inner_function()
    return result

# Example Usage:
result_value = outer_function()
print(f"Result: {result_value}")