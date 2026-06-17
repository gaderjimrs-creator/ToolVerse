from .calculator import calculator, Calculator, CALCULATOR
from .conversion_tools import conversiontools, ConversionTools, CONVERSIONTOOLS
from .date_time_tools import datetimetools, DateTimeTools, DATETIMETOOLS
from .file_tools import filetools, FileTools, FILETOOLS
from .number_tools import numbertools, NumberTools, NUMBERTOOLS
from .password_tools import passwordtools, PasswordTools, PASSWORDTOOLS
from .random_tools import randomtools, RandomTools, RANDOMTOOLS
from .string_tools import stringtools, StringTools, STRINGTOOLS
from .student_tools import studenttools, StudentTools, STUDENTTOOLS
from .system_tools import systemtools, SystemTools, SYSTEMTOOLS
from .json_tools import jsontools, JsonTools, JSONTOOLS

__version__ = "1.3.0"

__all__ = [
    # Lowercase classes
    "calculator",
    "conversiontools",
    "datetimetools",
    "filetools",
    "numbertools",
    "passwordtools",
    "randomtools",
    "stringtools",
    "studenttools",
    "systemtools",
    "jsontools",

    # PascalCase aliases
    "Calculator",
    "CALCULATOR",
    "ConversionTools",
    "CONVERSIONTOOLS",
    "DateTimeTools",
    "DATETIMETOOLS",
    "FileTools",
    "FILETOOLS",
    "NumberTools",
    "NUMBERTOOLS",
    "PasswordTools",
    "PASSWORDTOOLS",
    "RandomTools",
    "RANDOMTOOLS",
    "StringTools",
    "STRINGTOOLS",
    "StudentTools",
    "STUDENTTOOLS",
    "SystemTools",
    "SYSTEMTOOLS",
    "JsonTools",
    "JSONTOOLS",
]