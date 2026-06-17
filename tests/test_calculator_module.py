from ToolVerse.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(10, 3) == 13

def test_sub():
    assert calc.sub(10, 3) == 7