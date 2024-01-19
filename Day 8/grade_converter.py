def grade_converter(numerical_grade):
    if numerical_grade >= 90:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 70:
        return 'C'
    elif numerical_grade >= 50:
        return 'D'
    else:
        return 'F'

# Get user input for numerical grade
user_input = input("Enter your numerical grade: ")
numerical_grade = float(user_input)

# Call the function with the user's numerical grade
letter_grade = grade_converter(numerical_grade)

# Print the result
print(f"Numerical Grade: {numerical_grade}")
print(f"Letter Grade: {letter_grade}")
