import datetime
from commonutils import get_previous_weekday

def test_get_previous_weekday():
    # Test case 1: Monday
    date = datetime.date(2022, 1, 3)
    expected = datetime.date(2021, 12, 31)  # Previous Friday
    assert get_previous_weekday(date) == expected

    # Test case 2: Tuesday
    date = datetime.date(2022, 1, 4)
    expected = datetime.date(2022, 1, 3)  # Previous Monday
    assert get_previous_weekday(date) == expected

    # Test case 3: Wednesday
    date = datetime.date(2022, 1, 5)
    expected = datetime.date(2022, 1, 4)  # Previous Tuesday
    assert get_previous_weekday(date) == expected

    # Test case 4: Thursday
    date = datetime.date(2022, 1, 6)
    expected = datetime.date(2022, 1, 5)  # Previous Wednesday
    assert get_previous_weekday(date) == expected

    # Test case 5: Friday
    date = datetime.date(2022, 1, 7)
    expected = datetime.date(2022, 1, 6)  # Previous Thursday
    assert get_previous_weekday(date) == expected

    # Test case 6: Saturday
    date = datetime.date(2022, 1, 8)
    expected = datetime.date(2022, 1, 7)  # Previous Friday
    assert get_previous_weekday(date) == expected

    # Test case 7: Sunday
    date = datetime.date(2022, 1, 9)
    expected = datetime.date(2022, 1, 7)  # Previous Friday
    assert get_previous_weekday(date) == expected

    print("All test cases pass")

test_get_previous_weekday()