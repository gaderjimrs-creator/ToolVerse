from ToolVerse.password_tools import PasswordTools

tool = PasswordTools()

def test_hash_password():
    hashed = tool.hash_password("hello")
    assert len(hashed) == 64

def test_verify_password():
    hashed = tool.hash_password("hello")
    assert tool.verify_password("hello", hashed) == True
