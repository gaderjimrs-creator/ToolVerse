class numbertools:
    def __init__(self):
        pass

    def is_even(self, number):
        return number % 2 == 0

    def is_odd(self, number):
        return number % 2 != 0

    def is_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    def prime_factors(self, number):
        factors = []
        for i in range(2, int(number ** 0.5) + 1):
            while number % i == 0:
                factors.append(i)
                number //= i
        if number > 1:
            factors.append(number)
        return factors    
    
    def is_perfect_square(self, number):
        return int(number ** 0.5) ** 2 == number
    
    def fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_sequence = [0, 1]
            for i in range(2, n):
                next_fib = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_fib)
            return fib_sequence
    
    def multiplication_table(self, number, up_to=10):
        table = []
        for i in range(1, up_to + 1):
            table.append(f"{number} x {i} = {number * i}")
        return table
    
    def decimal_to_binary(self, number):
        return bin(number)[2:]
    
    def binary_to_decimal(self, binary_str):
        return int(binary_str, 2)
    
    def factorial(self, number):
        if number < 0:
            return "Factorial of negative number is not allowed"
        elif number == 0 or number == 1:
            return 1
        else:
            result = 1
            for i in range(2, number + 1):
                result *= i
            return result

NumberTools = numbertools
NUMBERTOOLS = numbertools