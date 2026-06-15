import random
class MyRandomTools:
    def __init__(self):
        pass

    def random_integer(self, start, end):
        return random.randint(start, end)

    def random_float(self, start, end):
        return random.uniform(start, end)

    def random_choice(self, sequence):
        return random.choice(sequence)

    def random_sample(self, population, k):
        return random.sample(population, k)

    def shuffle_list(self, lst):
        random.shuffle(lst)
        return lst
    
    def generate_random_string(self, length=8):
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def random_number_with_digits(self, digits):
        if digits <= 0:
            return "Number of digits must be positive"
        start = 10 ** (digits - 1)
        end = (10 ** digits) - 1
        return random.randint(start, end)

    def dice_roll(self, sides=6):
        return random.randint(1, sides)

    def coin_flip(self):
        return random.choice(['Heads', 'Tails'])

    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    
    def random_date(self, start_year=2000, end_year=2020):
        from datetime import datetime, timedelta
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        return random_date.strftime("%Y-%m-%d")
    
    def random_password(self, length=12):
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
