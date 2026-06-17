class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self, a, b):
        self.a = a
        self.b = b
        result = self.a + self.b
        return result
        
    def mul(self, a, b):
        self.a = a
        self.b = b
        result = self.a * self.b
        return result
    
    def div(self, a, b):
        self.a = a
        self.b = b
        if self.b != 0:
            result = self.a / self.b
            return result
        else:
            return "Division by zero is not allowed"
        
    def sub(self, a, b):
        self.a = a
        self.b = b
        result = self.a - self.b
        return result
    
    def percentage(self, a, b):
        self.a = a
        self.b = b
        if self.b != 0:
            result = (self.a * self.b) / 100
            return result
        else:
            return "Percentage by zero is not allowed"

    def sqrt(self, a):
        self.a = a
        if self.a >= 0:
            result = self.a ** 0.5
            return result
        else:
            return "Square root of negative number is not allowed"

    def square(self, a):
        self.a = a
        result = self.a ** 2
        return result
    
    def power(self, a, b):
        self.a = a
        self.b = b
        result = self.a ** self.b
        return result

    def factorial(self, a):
        self.a = a
        if self.a < 0:
            return "Factorial of negative number is not allowed"
        elif self.a == 0 or self.a == 1:
            return 1
        else:
            result = 1
            for i in range(2, self.a + 1):
                result *= i
            return result
        
    def gcd(self, a, b):
        self.a = a
        self.b = b
        while self.b:
            self.a, self.b = self.b, self.a % self.b
        return abs(self.a)
    
    def lcm(self, a, b):
        self.a = a
        self.b = b
        if self.a == 0 or self.b == 0:
            return 0
        else:
            return abs(self.a * self.b) // self.gcd(self.a, self.b)
        
    def hcf(self, a, b):
        return self.gcd(a, b)
    
    def lcm_hcf(self, a, b):
        hcf = self.hcf(a, b)
        lcm = self.lcm(a, b)
        return hcf, lcm
    
    def is_prime(self, a):
        self.a = a
        if self.a <= 1:
            return False
        for i in range(2, int(self.a ** 0.5) + 1):
            if self.a % i == 0:
                return False
        return True
    
    def prime_factors(self, a):
        self.a = a
        factors = []
        for i in range(2, int(self.a ** 0.5) + 1):
            while self.a % i == 0:
                factors.append(i)
                self.a //= i
        if self.a > 1:
            factors.append(self.a)
        return factors
    
    def gst_calculator(self, price, gst_rate):
        self.price = price
        self.gst_rate = gst_rate
        gst_amount = (self.price * self.gst_rate) / 100
        total_price = self.price + gst_amount
        return gst_amount, total_price
    
    def discount_calculator(self, price, discount_rate):
        self.price = price
        self.discount_rate = discount_rate
        discount_amount = (self.price * self.discount_rate) / 100
        final_price = self.price - discount_amount
        return discount_amount, final_price
    
    def simple_interest(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time
        interest = (self.principal * self.rate * self.time) / 100
        return interest
    
    def compound_interest(self, principal, rate, time, n=1):
        self.principal = principal
        self.rate = rate
        self.time = time
        self.n = n
        amount = self.principal * (1 + (self.rate / (100 * self.n))) ** (self.n * self.time)
        return amount - self.principal
    
    def percentage_increase(self, original, new):
        self.original = original
        self.new = new
        if self.original != 0:
            increase = self.new - self.original
            percentage_increase = (increase / self.original) * 100
            return percentage_increase
        else:
            return "Original value cannot be zero for percentage increase calculation"
    
    def percentage_decrease(self, original, new):
        self.original = original
        self.new = new
        if self.original != 0:
            decrease = self.original - self.new
            percentage_decrease = (decrease / self.original) * 100
            return percentage_decrease
        else:
            return "Original value cannot be zero for percentage decrease calculation"
    
    def average(self, numbers):
        self.numbers = numbers
        if len(self.numbers) > 0:
            return sum(self.numbers) / len(self.numbers)
        else:
            return "No numbers provided for average calculation"
    
    def median(self, numbers):
        self.numbers = sorted(numbers)
        n = len(self.numbers)
        if n % 2 == 0:
            median = (self.numbers[n // 2 - 1] + self.numbers[n // 2]) / 2
        else:
            median = self.numbers[n // 2]
        return median
    
    def mode(self, numbers):
        self.numbers = numbers
        from collections import Counter
        count = Counter(self.numbers)
        mode_data = count.most_common()
        mode = [num for num, freq in mode_data if freq == mode_data[0][1]]
        return mode
    