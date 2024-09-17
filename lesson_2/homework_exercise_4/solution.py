numbers_string = "2.5, -22, 1, 73.9, 34.99, 0, 4, 17, 95, 40, 8.0, 12, -64.2"

# Split the string into individual numbers and convert to floats
numbers = [float(num) for num in numbers_string.split(", ")]

# Initialize lists to collect numbers
no_remainder_by_2 = []
remainder_by_2 = []
no_remainder_by_3 = []
remainder_by_3 = []

# Iterate over the numbers and classify them
for num in numbers:
    if num % 2 == 0:
        no_remainder_by_2.append(num)
    else:
        remainder_by_2.append(num)

    if num % 3 == 0:
        no_remainder_by_3.append(num)
    else:
        remainder_by_3.append(num)

# Convert lists to comma-separated strings
no_remainder_by_2_str = ", ".join(map(str, no_remainder_by_2))
remainder_by_2_str = ", ".join(map(str, remainder_by_2))
no_remainder_by_3_str = ", ".join(map(str, no_remainder_by_3))
remainder_by_3_str = ", ".join(map(str, remainder_by_3))

# Print the results
print(f"Numbers with no remainder by 2: {no_remainder_by_2_str}") # Numbers with no remainder by 2: -22.0, 0.0, 4.0, 40.0, 8.0, 12.0
print(f"Numbers with remainder by 2: {remainder_by_2_str}") # Numbers with remainder by 2: 2.5, 1.0, 73.9, 34.99, 17.0, 95.0, -64.2
print(f"Numbers with no remainder by 3: {no_remainder_by_3_str}") # Numbers with no remainder by 3: 0.0, 12.0
print(f"Numbers with remainder by 3: {remainder_by_3_str}") # Numbers with remainder by 3: 2.5, -22.0, 1.0, 73.9, 34.99, 4.0, 17.0, 95.0, 40.0, 8.0, -64.2