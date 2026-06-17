from ToolVerse.system_tools import systemtools

tool = systemtools()

def test_os_name():
    assert isinstance(tool.get_os_name(), str)

def test_cpu_count():
    assert tool.get_cpu_count() > 0
