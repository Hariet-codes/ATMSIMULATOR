import string
import os
import getpass

# Create lists of users, pins and bank statements
users = ['matthew', 'cathrine', 'lucas', 'anne', 'anthony', 'patience']
pins = ['1234', '3456', '5678', '1256', '7880', '5788']
amounts = [4000, 3000, 2500, 7000, 5000, 1300]  # Use integers not strings
count = 0

# ===== CHECK EXISTENCE OF ENTERED USERNAME =====
while True:
    user = input('\nENTER USERNAME: ').lower().strip()

    if user in users:
        n = users.index(user)  # Get index directly - no need for if/elif chain
        break
    else:
        print('- - - - - - -')
        print('*************')
        print('INVALID USERNAME')
        print('*************')
        print('- - - - - - -')

# ===== PIN VALIDATION =====
count = 0
MAX_ATTEMPTS = 3

while count < MAX_ATTEMPTS:
    print('- - - - - -')
    print('***********')
    pin = getpass.getpass('PLEASE ENTER PIN: ')
    print('***********')
    print('- - - - - -')

    if pin.isdigit() and len(pin) == 4:   # Fixed: added () to isdigit, added colon
        if pin == pins[n]:                 # Fixed: added colon
            print('- - - - - -')
            print('***********')
            print(f'LOGIN SUCCESSFUL! WELCOME, {users[n].capitalize()}!')  # Fixed: capitalize()
            print('***********')
            print('- - - - - -')
            break                          # Fixed: added break after successful login
        else:
            count += 1
            remaining = MAX_ATTEMPTS - count
            print('- - - - - - -')
            print('*************')
            print('INVALID PIN')
            if remaining > 0:              # Fixed: capital I in If → if
                print(f'Attempts remaining: {remaining}')
            print('*************')
            print('- - - - - - -')
    else:
        count += 1                         # Fixed: also increment count for invalid format
        print('- - - - - - -')
        print('*************')
        print('PIN MUST BE 4 DIGITS')
        print('*************')
        print('- - - - - - -')

# ===== CHECK IF ACCOUNT IS LOCKED =====
if count == MAX_ATTEMPTS:                  # Fixed: moved outside while loop
    print('- - - - - - -')
    print('*************')
    print('ACCOUNT LOCKED DUE TO TOO MANY FAILED ATTEMPTS')  # Fixed: \Account → correct string
    print('*************')
    print('- - - - - - -')
    exit()

# ===== MAIN MENU =====
while True:                                # Fixed: While → while
    print('- - - - - - -')
    print('*************')
    print('SELECT FROM THE FOLLOWING OPTIONS:')  # Fixed: 'FROMMTHE' typo
    print('Balance _ _ _ _ _ _ _ _ (S)')
    print('Withdraw _ _ _ _ _ _ _ _ (W)')
    print('Deposit _ _ _ _ _ _ _ _ (L)')
    print('Change PIN _ _ _ _ _ _ _ (P)')   # Fixed: 'Chnage' typo
    print('Log out _ _ _ _ _ _ _ _ (Q)')    # Fixed: 'Loh=g out' typo
    print('*************')
    print('- - - - - - -')

    response = input('Enter choice: ').lower().strip()

    # ===== CHECK BALANCE =====
    if response == 's':                    # Fixed: 'S' → 's' (input is lowercased)
        print('- - - - - -')
        print('**********')
        print(f'{users[n].capitalize()}, YOU HAVE {amounts[n]:,} SHILLINGS ON YOUR ACCOUNT.')  # Fixed: {:,} for thousands
        print('**********')
        print('- - - - - -')

    # ===== WITHDRAW =====
    elif response == 'w':                  # Fixed: 'W' → 'w', if → elif
        print('- - - - - -')
        print('**********')
        try:
            cash_out = int(input('ENTER AMOUNT TO WITHDRAW: '))  # Fixed: 'AMMOUNT' typo
            print('**********')
            print('- - - - - -')

            if cash_out <= 0:              # Fixed: added colon
                print('- - - - - -')
                print('**********')
                print('AMOUNT MUST BE GREATER THAN 0')   # Fixed: 'AMMOUNT' typo
                print('**********')
                print('- - - - - -')
            elif cash_out > amounts[n]:    # Fixed: added colon
                print('- - - - - -')
                print('**********')
                print('INSUFFICIENT FUNDS')
                print('**********')
                print('- - - - - -')
            else:
                amounts[n] -= cash_out
                print('- - - - - -')
                print('**********')
                print('WITHDRAWAL SUCCESSFUL!')   # Fixed: 'SUCCESFUL' typo
                print(f'NEW BALANCE: {amounts[n]:,} SHILLINGS')
                print('**********')
                print('- - - - - -')

        except ValueError:                 # Fixed: moved except to directly after try block
            print('- - - - - -')
            print('**********')
            print('PLEASE ENTER A VALID NUMBER')
            print('**********')
            print('- - - - - -')

    # ===== DEPOSIT =====
    elif response == 'l':                  # Fixed: 'L' → 'l', if → elif
        print('- - - - - -')
        print('**********')
        try:
            cash_in = int(input('ENTER AMOUNT TO DEPOSIT: '))   # Fixed: said WITHDRAW instead of DEPOSIT
            print('**********')
            print('- - - - - -')

            if cash_in <= 0:               # Fixed: added colon
                print('- - - - - -')
                print('**********')
                print('AMOUNT TO DEPOSIT MUST BE GREATER THAN 0')
                print('**********')
                print('- - - - - -')
            else:
                amounts[n] += cash_in
                print('- - - - - -')
                print('**********')
                print('DEPOSIT SUCCESSFUL!')    # Fixed: said WITHDRAWAL instead of DEPOSIT
                print(f'NEW BALANCE: {amounts[n]:,} SHILLINGS')
                print('**********')
                print('- - - - - -')

        except ValueError:                 # Fixed: moved except directly after try block
            print('- - - - - -')
            print('**********')
            print('PLEASE ENTER A VALID NUMBER')
            print('**********')
            print('- - - - - -')

    # ===== CHANGE PIN =====
    elif response == 'p':                  # Fixed: 'P' → 'p', added colon
        print('- - - - - -')
        print('**********')
        new_pin = getpass.getpass('ENTER NEW PIN: ')
        print('**********')
        print('- - - - - -')

        # Validate new PIN
        if not new_pin.isdigit():          # Fixed: indentation
            print('- - - - - -')
            print('**********')
            print('PIN MUST CONSIST OF 4 DIGITS ONLY')
            print('**********')
            print('- - - - - -')
        elif len(new_pin) != 4:            # Fixed: added colon
            print('- - - - - -')
            print('**********')
            print('PIN MUST BE EXACTLY 4 DIGITS')   # Fixed: 'DIDGITS' typo
            print('**********')
            print('- - - - - -')
        elif new_pin == pins[n]:           # Fixed: added colon
            print('- - - - - -')
            print('**********')
            print('NEW PIN MUST BE DIFFERENT FROM OLD PIN')
            print('**********')
            print('- - - - - -')
        else:
            # Confirm new PIN
            new_ppin = getpass.getpass('CONFIRM NEW PIN: ')
            if new_ppin != new_pin:
                print('- - - - - -')
                print('**********')
                print('PIN MISMATCH')
                print('**********')
                print('- - - - - -')
            else:
                pins[n] = new_pin          # Fixed: == (comparison) → = (assignment)
                print('- - - - - -')
                print('**********')
                print('NEW PIN SAVED!')
                print('**********')
                print('- - - - - -')

    # ===== LOG OUT =====
    elif response == 'q':                  # Fixed: 'Q' → 'q'
        print('- - - - - -')
        print('**********')
        print(f'GOODBYE, {users[n].capitalize()}!')  # Fixed: missing f-string prefix
        print('**********')
        print('- - - - - -')
        break

    # ===== INVALID RESPONSE =====
    else:
        print('**********')
        print('INVALID RESPONSE')
        print('**********')

    print()  # Spacing between operations