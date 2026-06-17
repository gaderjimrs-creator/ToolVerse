from ToolVerse.random_tools import RandomTools

tool = RandomTools()

def test_random_integer():
    result = tool.random_integer(1, 10)
    assert 1 <= result <= 10

def test_dice_roll():
    result = tool.dice_roll()
    assert 1 <= result <= 6
