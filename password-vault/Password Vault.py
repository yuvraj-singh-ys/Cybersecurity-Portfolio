import sys
print("Welcome to your personal Password Vault!")
account_and_password = {'Google': 'f283fhy',
                        'Microsoft': '2366mkg', 'School_Account': '344gi2'}

# Functions:


def password_check(password, dictionary, account, mode='add'):

    action = "added" if mode == 'add' else "changed"

    # Same password/password used before check:
    while password in dictionary.values():
        confirm = input(
            "You have already used this password before. Are you sure you want to use it again? (Enter Y for yes and N for no): ")
        if confirm in ('Y', 'y'):
            break
        elif confirm in ('N', 'n'):
            password = input("Enter another password: ")
        else:
            print("Invalid input. Please enter Y or N.")

    # Length Check:
    while len(password) < 8:
        password = input(
            "Password must be at least 8 characters. Enter a new password: ")

    # Common Passwords Check:
    common_passwords = ['password', '12345678',
                        'password123', 'admin123', 'welcome123', 'abc123']
    while password.casefold() in [pword.casefold() for pword in common_passwords]:
        confirm = input(
            "This is a very common password. Use it anyway? (Y/N): ")
        if confirm in ('Y', 'y'):
            break
        elif confirm in ('N', 'n'):
            password = input("Enter a new password: ")
        else:
            print("Invalid input.")

    # Account Name in Passwords Check:
    while password.casefold() == account.casefold():
        confirm = input(
            "Password cannot be the same as the account name. Use it anyway? (Y/N): ")
        if confirm in ('Y', 'y'):
            break
        elif confirm in ('N', 'n'):
            password = input("Enter a new password: ")
        else:
            print("Invalid input.")

    # Sequential Characters:
    seq_char = ['123', 'abc', 'qwerty', 'asdf']
    found = False
    for i in seq_char:
        if i in password.casefold():
            found = True
            confirm2 = input(
                "This password contains some common sequences. Proceed anyway? (Yes/No): ")
            if confirm2 in ('Yes', 'yes'):
                break
            elif confirm2 in ('No', 'no'):
                password = input("Please type a new password: ")
                break
            else:
                print("Invalid input.")

    # Save and print summary
    dictionary[account] = password
    print(f"Account has been {action}.")

    # Summary
    if password not in dictionary.values() or (password in dictionary.values() and list(dictionary.values()).count(password) == 1):
        print("Password is original and has not been used before.✅")
    else:
        print("Password has been used before.⚠️")
    if len(password) >= 8:
        print("Password is greater than or equal to 8 characters.✅")
    else:
        print("Password is less than 8 characters.⚠️")
    if password.casefold() not in [pword.casefold() for pword in common_passwords]:
        print("Password is not a common password.✅")
    else:
        print("Password is a common password.⚠️")
    if password.casefold() != account.casefold():
        print("Password is not the same as the account name.✅")
    else:
        print("Password is the same as the account name.⚠️")
    if not found:
        print("Password does not contain common sequences.✅")
    else:
        print("Password contains common sequences.⚠️")


while True:
    task = input("Would you like to 'Add an account' (enter A), 'Retrieve a password' (enter B), 'List all accounts' (enter C), 'Delete an account' (enter D), 'Change password' (enter E) or 'Quit'? (enter F): ")

    # Task A:
    if task == 'A':
        new_acc = input("Please enter the name of your new account: ")
        if new_acc in account_and_password:
            print("This account is already in your dictionary.")
        else:
            new_pass = input("Please enter the password of your new account: ")
            password_check(new_pass, account_and_password, new_acc, mode='add')

    # Task B:
    elif task == 'B':
        repass = input("Please enter the account name: ")
        if repass in account_and_password:
            print(
                f"Here is your password for this account: {account_and_password[repass]}")
        else:
            print("That account is not in my database.")

    # Task C:
    elif task == 'C':
        for i in account_and_password.keys():
            print(i)

    # Task D:
    elif task == 'D':
        delacc = input("What account would you like to delete? ")
        if delacc in account_and_password:
            del account_and_password[delacc]
            print("Account deletion successful")
        else:
            print("That account is not in my database")

    # Task E:
    elif task == 'E':
        edacc = input(
            "Enter the name of the account whose password you wish to change: ")
        if edacc in account_and_password:
            edpass = input("Enter a new password: ")
            password_check(edpass, account_and_password, edacc, mode='change')
        else:
            print("This account is not in my database.")

    # Task F:
    elif task == 'F':
        sys.exit()

    # Exit:
    else:
        print("Invalid response.")
