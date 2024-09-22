

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

# and here is some code to test your implementation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_stats = NumberStats(numbers)
print(my_stats.min()) # 1
print(my_stats.max()) # 10
print(my_stats.average()) # 5.5
print(my_stats.all()) # {'min': 1, 'max': 10, 'average': 5.5}