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

def menu():
    """Main menu"""
    print()
    time.sleep(0.1)
    print("      [green]___[/] [bright_cyan]MENU[/] [green]___[/]")
    time.sleep(0.1)
    print()
    print("      [cyan]1. BALANCE[/]")
    time.sleep(0.1)
    print("      [cyan]2. DEPOSIT[/]")
    time.sleep(0.1)
    print("      [cyan]3. WITHDRAW[/]")
    time.sleep(0.1)
    print("      [cyan]0. EXIT[/]")
    time.sleep(0.1)
    print()
    print("[green]==================================================[/]")
    time.sleep(0.1)

loader()
def atm():
    """Verification"""
    pin = "1234"
    attempts = 0
    balance = 9999
    while attempts < 4:
        logo()
        print()
        entered_pin = input("      Enter your PIN: ")

        if entered_pin != pin:
            attempts += 1
            left = 4 - attempts
            print()
            print("      [cyan]Incorrect PIN[/]")
            time.sleep(0.1)
            print(f'      [cyan]Remaining attempts:[/] [red]{left}[/]')
            time.sleep(0.5)
            continue

        print()
        print("      [cyan]PIN accepted[/]")
        print()
        time.sleep(0.1)
        print("      [cyan]Access granted[/]")
        print()
        time.sleep(0.1)
        print("      [cyan]Loading menu...[/]")
        time.sleep(2)
        break

    if attempts == 4:
        print()
        print("      [cyan]Maximum PIN attempts reached[/]")
        time.sleep(0.1)
        print("      [cyan]Your card is locked[/]")
        print()
        time.sleep(0.1)
        print("      [cyan]Closing...[/]")
        time.sleep(2)
        return
    while True:
        """ Main loop"""
        logo()
        menu()
        print()
        choice = input("      Enter your choice: ")

        if not choice.isdigit():
            print()
            time.sleep(0.1)
            print("      [cyan]Invalid input[/]")
            print()
            time.sleep(0.1)
            print("      [cyan]Please enter a number[/]")
            time.sleep(1)
            continue

        choice = int(choice)

        if choice == 1:
            print()
            time.sleep(0.1)
            print("      [cyan]Account balance[/]")
            print()
            time.sleep(0.1)
            print(f'      [cyan]$[/] [red]{balance}[/]')
            time.sleep(2)
        elif choice == 2:
            print()
            amount = input("      Enter the amount to deposit: ")
            if not amount.isdigit():
                print()
                time.sleep(0.1)
                print("      [cyan]Invalid input[/]Please enter a number")
                time.sleep(0.1)
                print()
                print("      [cyan]Please enter only numbers[/]")
                time.sleep(1)
                continue
            amount = float(amount)
            balance += amount
            print()
            time.sleep(0.1)
            print("      [cyan]Deposit successful[/]")
            print()
            time.sleep(0.1)
            print(f'      [cyan]Your balance is:[/] [red]{balance}[/]')
            time.sleep(1)
        elif choice == 3:
            print("Withdraw")
        elif choice == 0:
            print("Thank you for using the atm. Goodbye!")
            break
        else:
            print()
            time.sleep(0.1)
            print("      [cyan]Invalid choice[/]")
            print()
            time.sleep(0.1)
            print("      [cyan]Please try again[/]")
            time.sleep(1)

atm()
