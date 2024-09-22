# Exercise 3

class RandomNumberGenerator:
    def __init__(self, n, min, max):
        self.n = n
        self.min = min
        self.max = max

    def generate_numbers(self):
        from random import randint
        return [randint(self.min, self.max) for _ in range(self.n)]

class NumberStats:
    def __init__(self, numbers):
        self.numbers = numbers

    def min(self):
        return min(self.numbers)

    def max(self):
        return max(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def all(self):
        return {
            'min': self.min(),
            'max': self.max(),
            'average': self.average()
        }

my_numbers = RandomNumberGenerator(10, 0, 15)
numbers = my_numbers.generate_numbers()
my_stats = NumberStats(numbers)
print(my_stats.all())
