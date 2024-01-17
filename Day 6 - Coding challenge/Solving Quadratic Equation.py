import cmath  # Importing the complex math module for handling complex roots

def solve_quadratic_equation(a, b, c):
    #ax^2+bx+c
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two solutions using the quadratic formula
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)

    return root1, root2

# Get coefficients from the user
a = float(input("Enter the coefficient 'x^2': "))
b = float(input("Enter the coefficient 'x': "))
c = float(input("Enter the constant 'c': "))

# Solve the quadratic equation
roots = solve_quadratic_equation(a, b, c)

# Display the roots
print("Root 1:", roots[0])
print("Root 2:", roots[1])
