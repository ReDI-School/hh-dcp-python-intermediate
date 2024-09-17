def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [str(num) for num in range(121) if is_prime(num)]
prime_numbers_str = ' '.join(prime_numbers)

print(f"Prime numbers between 0 and 120 are: '{prime_numbers_str}'") # Prime numbers between 0 and 120 are: '2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113'
