from ToolVerse.student_tools import studenttools

tool = studenttools()

def test_add_student():
    tool.add_student(1, "Ayaz", 17)
    assert tool.count_students() == 1

def test_get_student():
    assert tool.get_student(1)["name"] == "Ayaz"
