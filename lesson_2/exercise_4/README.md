# Exercise 4

You have following list of numbers defined as a single string:

"11,234,4,1000,4,69,54,50,82,532,176,36,148,2678,390,408,612,700"

Find the largest number in the list and print it to the console using string formatting (Format: "The largest number is x.")
Find the lowest number in the list and print it to the console using string formatting (Format: "The lowest number is x.")
Calculate the total of all numbers in the list and print it to the console using string formatting (Format: "The sum of numbers is x.")
Hints:

Use str.split(",") function to get the numbers out of string
Don't forget to cast the extracted number to int to avoid TypeError
Use f-strings or str.format() function to format the string

### Example
```python
numbers = "11,234,4,1000,4,69,54,50,82,532,176,36,148,2678,390,408,612,700"

# put your code here

print(f"The largest number is {largest}.") # Largest: 2678.
print(f"The lowest number is {lowest}.") # Lowest: 4.
print(f"The sum of numbers is {total}.") # Total: 7188.
```