from ToolVerse.date_time_tools import DateTimeTools

tool = DateTimeTools()

def test_days_between_dates():
    assert tool.days_between_dates(
        "2026-01-01",
        "2026-01-11"
    ) == 10

def test_leap_year():
    assert tool.is_leap_year(2024) == True
