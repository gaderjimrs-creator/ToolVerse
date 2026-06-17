from ToolVerse.calculator import calculator

calc = calculator()

def test_add():
    assert calc.add(10, 3) == 13

def test_sub():
    assert calc.sub(10, 3) == 7