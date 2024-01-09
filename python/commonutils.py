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

def get_env_var(key: str) -> str:
    """Returns the value of an environment variable"""
    import os
    try:
        print("Getting environment variable: " + key)
        return os.environ[key]
    except KeyError:
        print("Environment variable not found: " + key)
        return None

def save_to_file(content: str, filename: str) -> None:
    """Saves content to a file"""
    print("Saving to file: " + filename)
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename: str) -> str:
    """Reads content from a file"""
    print("Reading from file: " + filename)
    with open(filename, 'r') as file:
        content = file.read()
        return content