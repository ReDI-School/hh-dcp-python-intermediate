# Solution 1 - using a for loop

total = 0
for number in range(5, 1001, 10):
    total += number

print(f"The total of all numbers in the range 0...1000 is {total}.")


# Solution 2 - using the sum function

print(f"The total of all numbers in the range 0...1000 is {sum(range(5, 1001, 10))}.")

# Solution 3 - using a for loop and string manipulation

total = 0
for number in range(0, 1001):
    if str(number)[-1] == "5":
        total += number

print(f"The total of all numbers in the range 0...1000 is {total}.")