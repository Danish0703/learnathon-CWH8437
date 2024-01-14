# Python code using if, elif, else, and match case

def check_number_category(number):
    if number == 0:
        print("The number is zero.")
    elif number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def check_grade(score):
    match score:
        case 90 <= score <= 100:
            print("A")
        case 80 <= score < 90:
            print("B")
        case 70 <= score < 80:
            print("C")
        case 60 <= score < 70:
            print("D")
        case score < 60:
            print("F")
        case _:
            print("Invalid score")

# Example usage:
number_to_check = 17
check_number_category(number_to_check)

grade_to_check = 85
check_grade(grade_to_check)
