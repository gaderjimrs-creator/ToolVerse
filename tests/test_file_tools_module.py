from ToolVerse.file_tools import filetools

tool = filetools()


def test_write_and_read_file(tmp_path):
    file_path = tmp_path / "test.txt"

    tool.write_file(file_path, "Hello World")

    assert tool.read_file(file_path) == "Hello World"


def test_file_exists(tmp_path):
    file_path = tmp_path / "sample.txt"

    tool.create_file(file_path)

    assert tool.file_exists(file_path) == True


def test_count_lines(tmp_path):
    file_path = tmp_path / "lines.txt"

    tool.write_file(file_path, "A\nB\nC")

    assert tool.count_lines(file_path) == 3


def test_get_file_extension():
    assert tool.get_file_extension("hello.txt") == ".txt"


def test_delete_file(tmp_path):
    file_path = tmp_path / "delete.txt"

    tool.create_file(file_path)

    tool.delete_file(file_path)

    assert tool.file_exists(file_path) == False
