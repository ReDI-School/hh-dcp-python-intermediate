class RandomNumbers:
    def __init__(self, n, min, max):
        self.n = n
        self.min = min
        self.max = max


    def generate_numbers(self):
        import random
        return [random.randint(self.min, self.max) for _ in range(self.n)]


my_numbers = RandomNumbers(10, 1, 100)
print(my_numbers.generate_numbers())