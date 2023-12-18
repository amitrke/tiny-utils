import datetime

# Date Utils

def get_previous_weekday(date: datetime.date) -> datetime.date:
    """Get the previous weekday date from the given date"""
    return date - datetime.timedelta(days=1 if date.weekday() == 0 else date.weekday())