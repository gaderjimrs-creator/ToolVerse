class passwordtools:
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

PasswordTools = passwordtools
PASSWORDTOOLS = passwordtools