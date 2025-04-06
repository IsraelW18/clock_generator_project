import os
# import time
from clock_generator.time_gen import gen_time
from clock_generator.date_gen import gen_date
from clock_generator.utils import clear_console

def gen_date_and_time():
    """Combines date and time generators into a single generator."""
    for date in gen_date():
        for time in gen_time():
            yield f'{date} {time}'

def main():
    """Runs the combined date-time generator with periodic screen updates."""
    get_date_gen = gen_date_and_time()
    for i in range(0, 1000000000):
        if i % 1000000 == 0:
            clear_console()
            print(f'🕒 {next(get_date_gen)}')
            # time.sleep()
        else:
            next(get_date_gen)
            continue

if __name__ == "__main__":
    main()
