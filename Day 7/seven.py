# Example: Using for loop, while loop, break, and continue

# For loop to iterate over a sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Processing fruit: {fruit}")
    if fruit == "banana":
        break  # Break the loop if 'banana' is encountered

# While loop with continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping 3")
        continue  # Skip iteration when count is 3
    print(f"Count: {count}")

print("End of the program")
