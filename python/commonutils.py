import datetime

# Date Utils

def get_previous_weekday(inputDate: datetime.date) -> datetime.date:
    """Returns the date of the previous weekday (Mon-Fri)"""
    # Monday = 0, Sunday = 6
    if inputDate.weekday() == 0:
        return inputDate - datetime.timedelta(days=3)
    elif inputDate.weekday() == 6:
        return inputDate - datetime.timedelta(days=2)
    else:
        return inputDate - datetime.timedelta(days=1)

