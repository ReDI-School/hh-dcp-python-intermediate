# Exercise 3 Solution

# Use import for code reference
from lesson_5.exercise_3.main import RandomNumberGenerator, NumberStats

# Or rewrite the classes here
# class RandomNumberGenerator:
#     def __init__(self, n, min, max):
#         self.n = n
#         self.min = min
#         self.max = max
#
#     def generate_numbers(self):
#         from random import randint
#         return [randint(self.min, self.max) for _ in range(self.n)]
#
# class NumberStats:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def min(self):
#         return min(self.numbers)
#
#     def max(self):
#         return max(self.numbers)
#
#     def average(self):
#         return sum(self.numbers) / len(self.numbers)
#
#     def all(self):
#         return {
#             'min': self.min(),
#             'max': self.max(),
#             'average': self.average()
#         }

# Step 1: Create an instance of RandomNumberGenerator with n=10, min=0, max=15
rng1 = RandomNumberGenerator(10, 0, 15)
numbers1 = rng1.generate_numbers()

# Create an instance of NumberStats with the generated list
stats1 = NumberStats(numbers1)

# Print the dictionary returned by the all method of the NumberStats class
print(stats1.all())

# Step 2: Create another instance of RandomNumberGenerator with n=5, min=10, max=20
rng2 = RandomNumberGenerator(5, 10, 20)
numbers2 = rng2.generate_numbers()

# Print the dictionary returned by the all method of the NumberStats class without creating a new instance
print(stats1.all())  # The numbers have not changed because stats1 is still using the old list of numbers

# Step 3: Fix the numbers by creating a new instance of the NumberStats class with the new list of numbers
stats2 = NumberStats(numbers2)

# Print the dictionary returned by the all method of the NumberStats class
print(stats2.all())