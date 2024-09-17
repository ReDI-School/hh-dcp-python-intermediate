numbers = "11,234,4,1000,4,69,54,50,82,532,176,36,148,2678,390,408,612,700"
# put your code here
converted = list(map(lambda x: int(x), numbers.split(",")))
largest = max(converted)
lowest = min(converted)
total = sum(converted)


print(f"The largest number is {largest}.") # Largest: 2678.
print(f"The lowest number is {lowest}.") # Lowest: 4.
print(f"The sum of numbers is {total}.") # Total: 7188.
