"""
Digital bank virtual atm machine
"""
import os
import time
import datetime
from rich import print


def loader():
    """INTRO"""
    numbers = ['5%', '10%', '15%', '20%', '25%', '30%', '35%',
               '40%', '45%', '50%', '55%', '60%', '65%', '70%', 
               '75%', '80%', '85%', '90%', '95%', '100%']
    for number in numbers:
        os.system('cls||clear')
        print()
        print("[green]==================================================[/]")
        print()
        print(f'               [blue]LOADING {number}[/]')
        print()
        print("[green]==================================================[/]")
        time.sleep(0.1)

def logo():
    """Main welcome message, day, time, name"""
    time.sleep(1)
    os.system('cls||clear')
    print()
    now = datetime.datetime.now()
    print(now.strftime("      [cyan]%A       %Y-%m-%d  %H:%M:%S[/]"))
    time.sleep(0.1)
    print("[green]==================================================[/]")
    time.sleep(0.1)
    print()
    print("      [cyan]Welcome to[/]   [bright_magenta]DIGITAL BANK[/]")
    print()
    time.sleep(0.1)
    print("[green]==================================================[/]")
    time.sleep(0.1)

loader()
def atm():
    """Verification"""
    pin = "1234"
    attempts = 0
    while attempts < 4:
        logo()
        entered_pin = input("Enter your PIN: ")

        if entered_pin != pin:
            attempts += 1
            remaining_attempts = 4 - attempts
            print("Incorrect PIN. Please try again. Remaining attempts: ", remaining_attempts)
            continue

        print("PIN accepted. Access granted.")
        break

    if attempts == 4:
        print("maximum PIN attempts reached. Your card is locked.")
        return

atm()
