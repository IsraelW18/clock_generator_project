import os

def clear_console():
    """Clears the console screen for both Windows and Unix systems."""
    os.system('cls' if os.name == 'nt' else 'clear')
