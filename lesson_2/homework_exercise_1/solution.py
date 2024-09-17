numbers = "13,27,5,67,39,2,10,89,41,7,9,73"

# Split the string into a list of numbers
number_list = numbers.split(',')

# Increase each number by 2
new_number_list = [str(int(num) + 2) for num in number_list]

# Join the list back into a comma-separated string
new_numbers = ','.join(new_number_list)

# Print the result
print(new_numbers)  # Output: 15,29,7,69,41,4,12,91,43,9,11,75

# Alternative solution using list comprehension
print(','.join([str(int(num) + 2) for num in numbers.split(',')]))  # Output: 15,29,7,69,41,4,12,91,43,9,11,75

# Alternative solution using map and lambda
print(','.join(map(lambda x: str(int(x) + 2), numbers.split(','))))  # Output: 15,29,7,69,41,4,12,91,43,9,11,75