def gen_years(start=2019):
    """
    Yields (year, is_leap) tuples starting from a given year.
    """
    while True:
        is_leap = True if (start % 4 == 0 and start % 100 != 0) or (start % 400 == 0) else False
        yield start, is_leap
        start += 1

def gen_month():
    """Yields months from 01 to 12."""
    month = 1
    while month <= 12:
        yield f'{month:02d}'
        month += 1

def gen_days(month=int(), leap_year=True):
    """
    Yields day numbers as strings based on the month and leap year.
    """
    month = int(month)
    if month not in range(1, 13):
        yield "Error"
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        num_days = 31
    elif month in [4, 6, 9, 11]:
        num_days = 30
    elif month == 2:
        num_days = 29 if leap_year else 28

    for day in range(1, num_days + 1):
        yield f'{day:02d}'

def gen_date():
    """Yields full dates in YYYY/MM/DD format."""
    for year, is_leap in gen_years():
        for month in gen_month():
            for day in gen_days(month, is_leap):
                yield f'{year}/{month}/{day}'
