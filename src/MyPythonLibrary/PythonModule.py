import os
import random
import psutil

class MyCalculator:
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
class MyStringTools:
    def __init__(self):
        self.string = ""

    def set_string(self, string):
        self.string = string

    def get_string(self):
        return self.string

    def reverse_string(self):
        return self.string[::-1]

    def is_palindrome(self):
        return self.string == self.reverse_string()

    def to_uppercase(self):
        return self.string.upper()

    def to_lowercase(self):
        return self.string.lower()

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = sum(1 for char in self.string if char in vowels)
        return count

    def count_consonants(self):
        vowels = "aeiouAEIOU"
        count = sum(1 for char in self.string if char.isalpha() and char not in vowels)
        return count

    def count_words(self):
        words = self.string.split()
        return len(words)

    def count_characters(self):
        return len(self.string)

    def is_anagram(self, other_string):
        return sorted(self.string) == sorted(other_string)
    
    def capitalize_words(self):
        return ' '.join(word.capitalize() for word in self.string.split())
    
    def remove_spaces(self):
        return self.string.replace(" ", "")
class MyDateTimeTools:
    def __init__(self):
        pass

    def get_date(self):
        from datetime import date
        return date.today()

    def get_time(self):
        from datetime import datetime
        return datetime.now().time()

    def get_datetime(self):
        from datetime import datetime
        return datetime.now()

    def format_date(self, date_obj, format_str="%Y-%m-%d"):
        return date_obj.strftime(format_str)

    def format_time(self, time_obj, format_str="%H:%M:%S"):
        return time_obj.strftime(format_str)

    def format_datetime(self, datetime_obj, format_str="%Y-%m-%d %H:%M:%S"):
        return datetime_obj.strftime(format_str)
    
    def days_between_dates(self, start_date, end_date):
        from datetime import datetime
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        return delta.days
    
    def age_calculator(self, birth_date):
        from datetime import datetime
        birth = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age
    
    def add_days(self, date_str, days):
        from datetime import datetime, timedelta
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")
    
    def subtract_days(self, date_str, days):
        from datetime import datetime, timedelta
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj - timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")
    
    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def get_weekday(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A")
    
    def get_month_name(self, month_number):
        import calendar
        if 1 <= month_number <= 12:
            return calendar.month_name[month_number]
        else:
            return "Invalid month number"
        
    def get_day_of_year(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.timetuple().tm_yday
    
    def get_week_number(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.isocalendar()[1]
class MyFileTools:
    def __init__(self):
        pass

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def append_to_file(self, file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)

    def count_lines(self, file_path):
        with open(file_path, 'r') as file:
            return len(file.readlines())

    def count_words(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)

    def count_characters(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            return len(text)
    
    def find_and_replace(self, file_path, find_str, replace_str):
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.replace(find_str, replace_str)
        with open(file_path, 'w') as file:
            file.write(new_text)
    
    def create_file(self, file_path):
        with open(file_path, 'w') as file:
            pass  # Just create an empty file  
    
    def delete_file(self, file_path):
        import os
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            return "File does not exist"
    
    def file_exists(self, file_path):
        import os
        return os.path.exists(file_path)
    
    def get_file_size(self, file_path):
        import os
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        else:
            return "File does not exist"

    def get_file_extension(self, file_path):
        import os
        return os.path.splitext(file_path)[1]

    def list_files_in_directory(self, directory_path):
        import os
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            return os.listdir(directory_path)
        else:
            return "Directory does not exist"

    def copy_file(self, source_path, destination_path):
        import shutil
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
        else:
            return "Source file does not exist"
   
    def move_file(self, source_path, destination_path):
        import shutil
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            return "Source file does not exist" 
    
    def rename_file(self, old_path, new_path):
        import os
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        else:
            return "File does not exist"
class MyPasswordTools:
    def __init__(self):
        pass

    def generate_password(self, length=12):
        import random
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def password_strength(self, password):
        import re
        if len(password) < 8:
            return "Weak"
        elif re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[@$!%*?&]', password):
            return "Strong"
        else:
            return "Moderate"  
    
    def hash_password(self, password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password, hashed_password):
        return self.hash_password(password) == hashed_password
    
    def password_contains_uppercase(self, password):
        return any(char.isupper() for char in password)
    
    def password_contains_lowercase(self, password):
        return any(char.islower() for char in password)
    
    def password_contains_digit(self, password):
        return any(char.isdigit() for char in password)
    
    def password_contains_special_char(self, password):
        import string
        return any(char in string.punctuation for char in password)
    
    def password_length(self, password):
        return len(password)
    
    def generate_strong_password(self, length=12):
        while True:
            password = self.generate_password(length)
            if self.password_strength(password) == "Strong":
                return password
    
    def generate_password_with_criteria(self, length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
        import random
        import string
        characters = ''
        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if digits:
            characters += string.digits
        if special_chars:
            characters += string.punctuation
        if not characters:
            return "At least one character type must be selected"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def password_meets_criteria(self, password, uppercase=True, lowercase=True, digits=True, special_chars=True):
        if uppercase and not self.password_contains_uppercase(password):
            return False
        if lowercase and not self.password_contains_lowercase(password):
            return False
        if digits and not self.password_contains_digit(password):
            return False
        if special_chars and not self.password_contains_special_char(password):
            return False
        return True
    
    def generate_password_with_all_criteria(self, length=12):
        while True:
            password = self.generate_password(length)
            if self.password_meets_criteria(password):
                return password
    
    def generate_pin(self, length=4):
        import random
        digits = '0123456789'
        pin = ''.join(random.choice(digits) for _ in range(length))
        return pin
class MyNumberTools:
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
    
    def fectorial(self, number):
        if number < 0:
            return "Factorial of negative number is not allowed"
        elif number == 0 or number == 1:
            return 1
        else:
            result = 1
            for i in range(2, number + 1):
                result *= i
            return result
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
class MyConversionTools:
    def __init__(self):
        pass

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def kilometers_to_miles(self, kilometers):
        return kilometers * 0.621371

    def miles_to_kilometers(self, miles):
        return miles / 0.621371

    def pounds_to_kilograms(self, pounds):
        return pounds * 0.453592

    def kilograms_to_pounds(self, kilograms):
        return kilograms / 0.453592
    
    def inches_to_centimeters(self, inches):
        return inches * 2.54
    
    def centimeters_to_inches(self, centimeters):
        return centimeters / 2.54
    
    def liters_to_gallons(self, liters):
        return liters * 0.264172
    
    def gallons_to_liters(self, gallons):
        return gallons / 0.264172

    def kilograms_to_grams(self, kilograms):
        return kilograms * 1000

    def grams_to_kilograms(self, grams):
        return grams / 1000

    def meters_to_feet(self, meters):
        return meters * 3.28084

    def feet_to_meters(self, feet):
        return feet / 3.28084
        
    def centimeters_to_meters(self, centimeters):
        return centimeters / 100
    
    def meters_to_centimeters(self, meters):
        return meters * 100
    
    def meters_to_kilometers(self, meters):
        return meters / 1000
    
    def kilometers_to_meters(self, kilometers):
        return kilometers * 1000
    
    def seconds_to_minutes(self, seconds):
        return seconds / 60
    
    def minutes_to_seconds(self, minutes):
        return minutes * 60
    
    def hours_to_minutes(self, hours):
        return hours * 60
    
    def minutes_to_hours(self, minutes):
        return minutes / 60
    
    def days_to_weeks(self, days):
        return days / 7
    
    def weeks_to_days(self, weeks):
        return weeks * 7
    
    def years_to_months(self, years):
        return years * 12
    
    def months_to_years(self, months):
        return months / 12
    
    def years_to_days(self, years):
        return years * 365.25
    
    def days_to_years(self, days):
        return days / 365.25
    
    def hours_to_seconds(self, hours):
        return hours * 3600
    
    def seconds_to_hours(self, seconds):
        return seconds / 3600
    
    def liters_to_milliliters(self, liters):
        return liters * 1000
    
    def milliliters_to_liters(self, milliliters):
        return milliliters / 1000
    
    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15
    
    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    
    def kelvin_to_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9/5 + 32
class MyStudentTools:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age):
        self.students[student_id] = {'name': name, 'age': age}

    def get_student(self, student_id):
        return self.students.get(student_id, "Student not found")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            return "Student not found"

    def update_student(self, student_id, name=None, age=None):
        if student_id in self.students:
            if name is not None:
                self.students[student_id]['name'] = name
            if age is not None:
                self.students[student_id]['age'] = age
        else:
            return "Student not found"
    
    def list_students(self):
        return self.students
    
    def count_students(self):
        return len(self.students)
    
    def calculate_percentage(self, student_id, marks_obtained, total_marks):
        if student_id in self.students:
            percentage = (marks_obtained / total_marks) * 100
            self.students[student_id]['percentage'] = percentage
            return percentage
        else:
            return "Student not found"
        
    def calculate_grade(self, student_id):
        if student_id in self.students:
            percentage = self.students[student_id].get('percentage', None)
            if percentage is not None:
                if percentage >= 90:
                    grade = 'A'
                elif percentage >= 80:
                    grade = 'B'
                elif percentage >= 70:
                    grade = 'C'
                elif percentage >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                self.students[student_id]['grade'] = grade
                return grade
            else:
                return "Percentage not calculated for this student"
        else:
            return "Student not found"
    
    def calculate_cgpa(self, student_id, grades):
        if student_id in self.students:
            grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
            total_points = sum(grade_points.get(grade, 0) for grade in grades)
            gpa = total_points / len(grades)
            self.students[student_id]['gpa'] = gpa
            return gpa
        else:
            return "Student not found"
    
    def get_student_report(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            report = f"Student ID: {student_id}\n"
            report += f"Name: {student['name']}\n"
            report += f"Age: {student['age']}\n"
            report += f"Percentage: {student.get('percentage', 'Not calculated')}\n"
            report += f"Grade: {student.get('grade', 'Not calculated')}\n"
            report += f"GPA: {student.get('gpa', 'Not calculated')}\n"
            return report
        else:
            return "Student not found"
    
    def get_all_students_report(self):
        report = ""
        for student_id, student in self.students.items():
            report += f"Student ID: {student_id}\n"
            report += f"Name: {student['name']}\n"
            report += f"Age: {student['age']}\n"
            report += f"Percentage: {student.get('percentage', 'Not calculated')}\n"
            report += f"Grade: {student.get('grade', 'Not calculated')}\n"
            report += f"GPA: {student.get('gpa', 'Not calculated')}\n"
            report += "-------------------------\n"
        return report
    
    def get_top_student(self):
        top_student_id = None
        top_percentage = -1
        for student_id, student in self.students.items():
            percentage = student.get('percentage', None)
            if percentage is not None and percentage > top_percentage:
                top_percentage = percentage
                top_student_id = student_id
        if top_student_id is not None:
            return self.get_student_report(top_student_id)
        else:
            return "No students with calculated percentage"
    
    def get_bottom_student(self):
        bottom_student_id = None
        bottom_percentage = float('inf')
        for student_id, student in self.students.items():
            percentage = student.get('percentage', None)
            if percentage is not None and percentage < bottom_percentage:
                bottom_percentage = percentage
                bottom_student_id = student_id
        if bottom_student_id is not None:
            return self.get_student_report(bottom_student_id)
        else:
            return "No students with calculated percentage"
    
    def get_average_percentage(self):
        total_percentage = 0
        count = 0
        for student in self.students.values():
            percentage = student.get('percentage', None)
            if percentage is not None:
                total_percentage += percentage
                count += 1
        if count > 0:
            return total_percentage / count
        else:
            return "No students with calculated percentage"
    
    def get_average_gpa(self):
        total_gpa = 0
        count = 0
        for student in self.students.values():
            gpa = student.get('gpa', None)
            if gpa is not None:
                total_gpa += gpa
                count += 1
        if count > 0:
            return total_gpa / count
        else:
            return "No students with calculated GPA"
    
    def get_students_with_grade(self, grade):
        students_with_grade = []
        for student_id, student in self.students.items():
            if student.get('grade', None) == grade:
                students_with_grade.append(student_id)
        return students_with_grade
    
    def get_students_above_percentage(self, percentage):
        students_above = []
        for student_id, student in self.students.items():
            student_percentage = student.get('percentage', None)
            if student_percentage is not None and student_percentage > percentage:
                students_above.append(student_id)
        return students_above
    
    def get_students_below_percentage(self, percentage):
        students_below = []
        for student_id, student in self.students.items():
            student_percentage = student.get('percentage', None)
            if student_percentage is not None and student_percentage < percentage:
                students_below.append(student_id)
        return students_below
class MySystemTools:
    def __init__(self):
        pass

    def get_os_name(self):
        return os.name

    def get_current_working_directory(self):
        return os.getcwd()

    def list_directory_contents(self, path='.'):
        return os.listdir(path)

    def create_directory(self, path):
        os.makedirs(path, exist_ok=True)

    def remove_directory(self, path):
        os.rmdir(path)

    def get_environment_variable(self, var_name):
        return os.environ.get(var_name)

    def set_environment_variable(self, var_name, value):
        os.environ[var_name] = value

    def delete_environment_variable(self, var_name):
        if var_name in os.environ:
            del os.environ[var_name]
    
    def get_Python_version(self):
        import sys
        return sys.version
    
    def get_current_directory(self):
        return os.getcwd()
    
    def change_directory(self, path):
        os.chdir(path)
    
    def get_file_permissions(self, file_path):
        import stat
        if os.path.exists(file_path):
            permissions = stat.filemode(os.stat(file_path).st_mode)
            return permissions
        else:
            return "File does not exist"
    
    def set_file_permissions(self, file_path, mode):
        import os
        if os.path.exists(file_path):
            os.chmod(file_path, mode)
        else:
            return "File does not exist"
    
    def get_system_info(self):
        import platform
        return {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    
    def get_environment_variables(self):
        return dict(os.environ)
    
    def get_process_id(self):
        import os
        return os.getpid()
    
    def get_parent_process_id(self):
        import os
        return os.getppid()
    
    def get_user_id(self):
        import os
        return os.getuid() if hasattr(os, 'getuid') else None
    
    def get_group_id(self):
        import os
        return os.getgid() if hasattr(os, 'getgid') else None
    
    def get_current_user(self):
        import getpass
        return getpass.getuser()
    
    def get_home_directory(self):
        return os.path.expanduser("~")
    
    def get_temp_directory(self):
        import tempfile
        return tempfile.gettempdir()
    
    def get_current_timestamp(self):
        import time
        return time.time()
    
    def get_current_datetime(self):
        from datetime import datetime
        return datetime.now()
    
    def get_system_uptime(self):
        import time
        if hasattr(time, 'monotonic'):
            return time.monotonic()
        else:
            return "System uptime not available"
    
    def get_cpu_count(self):
        import os
        return os.cpu_count()
    
    def get_memory_info(self):
        import psutil
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "free": mem.free
        }
    
    def get_disk_usage(self, path='/'):
        import shutil
        total, used, free = shutil.disk_usage(path)
        return {
            "total": total,
            "used": used,
            "free": free
        }
    
    def get_network_info(self):
        net_if_addrs = psutil.net_if_addrs()
        net_if_stats = psutil.net_if_stats()
        network_info = {}
        for interface, addrs in net_if_addrs.items():
            network_info[interface] = {
                "addresses": [addr.address for addr in addrs],
                "is_up": net_if_stats[interface].isup if interface in net_if_stats else None
            }
        return network_info
    
    def get_system_load(self):
        import os
        if hasattr(os, 'getloadavg'):
            return os.getloadavg()
        else:
            return "System load not available"
    