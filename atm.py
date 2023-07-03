"""
Digital bank virtual atm machine
"""

def atm():
    """Verification"""
    pin = "1234"
    attempts = 0
    while attempts < 4:
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
