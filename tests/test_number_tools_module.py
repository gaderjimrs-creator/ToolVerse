from ToolVerse.number_tools import numbertools

tool = numbertools()

def test_even():
    assert tool.is_even(10) == True

def test_prime():
    assert tool.is_prime(7) == True

def test_binary():
    assert tool.decimal_to_binary(10) == "1010"
