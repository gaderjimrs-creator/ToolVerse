class datetimetools:
    def __init__(self):
        pass

    def get_date(self):
        from datetime import date
        return date.today()

    def get_time(self):
        from datetime import datetime
        return datetime.now().time()

    def get_datetime(self):
        from datetime import datetime
        return datetime.now()

    def format_date(self, date_obj, format_str="%Y-%m-%d"):
        return date_obj.strftime(format_str)

    def format_time(self, time_obj, format_str="%H:%M:%S"):
        return time_obj.strftime(format_str)

    def format_datetime(self, datetime_obj, format_str="%Y-%m-%d %H:%M:%S"):
        return datetime_obj.strftime(format_str)
    
    def days_between_dates(self, start_date, end_date):
        from datetime import datetime
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        return delta.days
    
    def age_calculator(self, birth_date):
        from datetime import datetime
        birth = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age
    
    def add_days(self, date_str, days):
        from datetime import datetime, timedelta
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")
    
    def subtract_days(self, date_str, days):
        from datetime import datetime, timedelta
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj - timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")
    
    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def get_weekday(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A")
    
    def get_month_name(self, month_number):
        import calendar
        if 1 <= month_number <= 12:
            return calendar.month_name[month_number]
        else:
            return "Invalid month number"
        
    def get_day_of_year(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.timetuple().tm_yday
    
    def get_week_number(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.isocalendar()[1]

DateTimeTools = datetimetools
DATETIMETOOLS = datetimetools