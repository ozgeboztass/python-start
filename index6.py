# Given list of numbers
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# Initialize an empty list to store valid numbers
valid_numbers = []

# Loop through the numbers list
for number in numbers:
    # Check if the number is between 0 and 100
    if 0 <= number <= 100:
        # Add the number to the valid_numbers list
        valid_numbers.append(number)

# Calculate the total of the valid numbers
total = sum(valid_numbers)

# Calculate the average of the valid numbers
average = total / len(valid_numbers) if valid_numbers else 0

# Printing the results
print("Valid Numbers:", valid_numbers)
print("Total:", total)
print("Average:", average)
