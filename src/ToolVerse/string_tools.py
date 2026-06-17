class stringtools:
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

StringTools = stringtools
STRINGTOOLS = stringtools