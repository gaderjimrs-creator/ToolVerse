# ToolVerse

A powerful Python utility library created by **Mohammed Ayaz**.
This library provides ready-to-use tools for calculations, string operations, number utilities, password generation, file handling, date & time operations, random generators, student management, system utilities, and more.

---

## Features

| Module           | Description                                     |
| ---------------- | ----------------------------------------------- |
| calculator       | Mathematical calculations and utility functions |
| conversion_tools | Unit and measurement conversions                |
| date_time_tools  | Date and time utilities                         |
| file_tools       | File management operations                      |
| number_tools     | Number-related utilities                        |
| password_tools   | Password generation and security tools          |
| random_tools     | Random values, strings, dates, and passwords    |
| string_tools     | String manipulation utilities                   |
| student_tools    | Student management and reporting system         |
| system_tools     | System and OS information utilities             |

---

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/gaderjimrs-creator/MyPythonLibrary.git
```

Or clone the repository:

```bash
git clone https://github.com/gaderjimrs-creator/MyPythonLibrary.git

cd MyPythonLibrary

pip install .
```

---

## Usage Examples

### Calculator

```python
from ToolVerse.calculator import MyCalculator

calc = MyCalculator()

print(calc.add(10, 5))
print(calc.sub(10, 5))
print(calc.mul(10, 5))
print(calc.div(10, 5))
```

### Password Generator

```python
from ToolVerse.password_tools import MyPasswordTools

pwd = MyPasswordTools()

print(pwd.generate_password())
print(pwd.generate_strong_password())
```

### String Tools

```python
from ToolVerse.string_tools import MyStringTools

s = MyStringTools()

s.set_string("Hello World")

print(s.reverse_string())
print(s.to_uppercase())
print(s.count_words())
```

---

## Modules Included

* calculator
* conversion_tools
* date_time_tools
* file_tools
* number_tools
* password_tools
* random_tools
* string_tools
* student_tools
* system_tools

---

## Running Tests

Run all tests using:

```bash
pytest
```

Expected result:

```bash
25 passed
```

---

## Project Structure

```text
MyPythonLibrary/
│
├── src/
│   └── MyPythonLibrary/
│
├── tests/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── pytest.ini
└── setup.py
```

---

## Continuous Integration

GitHub Actions automatically runs all tests on every push and pull request.

---

## License

This project is licensed under the terms of the LICENSE file included in this repository.

---

## Author

**Mohammed Ayaz**

GitHub:
https://github.com/gaderjimrs-creator

Python Developer | Open Source Enthusiast

