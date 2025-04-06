def gen_seconds():
    """Yields seconds from 0 to 59."""
    sec = 0
    while sec < 60:
        yield sec
        sec += 1

def gen_minutes():
    """Yields minutes from 0 to 59."""
    minute = 0
    while minute < 60:
        yield minute
        minute += 1

def gen_hours():
    """Yields hours from 0 to 23."""
    hour = 0
    while hour < 24:
        yield hour
        hour += 1

def gen_time():
    """Yields full time strings in HH:MM:SS format."""
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_seconds():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"
