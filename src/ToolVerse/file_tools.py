import os
import shutil

class filetools:
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
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            return "File does not exist"
    
    def file_exists(self, file_path):
        return os.path.exists(file_path)
    
    def get_file_size(self, file_path):
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        else:
            return "File does not exist"

    def get_file_extension(self, file_path):
        return os.path.splitext(file_path)[1]

    def list_files_in_directory(self, directory_path):
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            return os.listdir(directory_path)
        else:
            return "Directory does not exist"

    def copy_file(self, source_path, destination_path):
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
        else:
            return "Source file does not exist"
   
    def move_file(self, source_path, destination_path):
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            return "Source file does not exist" 
    
    def rename_file(self, old_path, new_path):
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        else:
            return "File does not exist"
