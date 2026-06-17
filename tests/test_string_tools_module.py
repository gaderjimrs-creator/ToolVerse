from ToolVerse.string_tools import StringTools

tool = StringTools()

def test_reverse_string():
    tool.set_string("hello")
    assert tool.reverse_string() == "olleh"

def test_palindrome():
    tool.set_string("madam")
    assert tool.is_palindrome() == True

def test_count_words():
    tool.set_string("hello world python")
    assert tool.count_words() == 3
