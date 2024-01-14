

age = int(input("Enter your age: "))
show_time = int(input("Enter the show time (in 24-hour format): "))

match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
       ticket_price =  0  # Free ticket for ages 0-5
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
       ticket_price =  10  # $10 ticket for ages 6-12
    case 13 | 14 | 15 | 16 | 17 | 18:
       ticket_price =  15  # $15 ticket for ages 13-18
    case _:
       ticket_price =  20  # $20 ticket for age 19 and above

# Apply discount for shows before 12:00 PM
if show_time < 12:
    ticket_price -= 5

print(f"The ticket price is ${ticket_price}.")
