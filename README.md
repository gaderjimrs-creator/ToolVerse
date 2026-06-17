# ToolVerse

A powerful Python utility library that provides ready-to-use tools for calculations, string manipulation, file handling, date and time operations, password generation, random utilities, student management, system information, and more.

## Installation

Install from PyPI:

```bash
pip install ToolVerse
```

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
| student_tools    | Student management and reporting utilities      |
| system_tools     | System and OS information utilities             |
| json_tools       | JSON read, write and validation utilities       |

## Quick Start

### Calculator

```python
from ToolVerse.calculator import calculator

calc = calculator()

print(calc.add(10, 5))
print(calc.sub(10, 5))
print(calc.mul(10, 5))
print(calc.div(10, 5))
```

### Password Generator

```python
from ToolVerse.password_tools import passwordtools

pwd = passwordtools()

print(pwd.generate_password())
print(pwd.generate_strong_password())
```

### String Tools

```python
from ToolVerse.string_tools import stringtools

s = stringtools()

s.set_string("Hello World")

print(s.reverse_string())
print(s.to_uppercase())
print(s.count_words())
```

### json tools

```python
from ToolVerse.json_tools import jsontools

jt = jsontools()

data = {
    "name": "Ayaz",
    "age": 17
}

jt.write_json("data.json", data)

print(jt.read_json("data.json"))

print(jt.validate_json('{"name":"Ayaz"}'))
```

## Running Tests

```bash
pytest
```

## Project Structure

```text
ToolVerse/
├── src/
│   └── ToolVerse/
├── tests/
├── README.md
├── LICENSE
├── pyproject.toml
├── pytest.ini
└── setup.py
```

## License

MIT License

## Repository

GitHub:
https://github.com/gaderjimrs-creator/MyPythonLibrary
