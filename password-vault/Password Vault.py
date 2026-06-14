import sys
print("Welcome to your personal Password Vault!")
account_and_password = {'Google': 'f283fhy', 'Microsoft': '2366mkg', 'School_Account': '344gi2'}

#Functions:

def password_check(password, dictionary, account):
    
#Same password/password used before check:
    
    while password in dictionary.values():
        confirm = input("You have already used this password before. Are you sure you want to use it again? (Enter Y for yes and N for no): ")
        if confirm in ('Y', 'y'):
            dictionary[account] = password
            print("Account has been added.")
            return
        elif confirm in ('N', 'n'):
            password = input("Enter another password: ")
        else:
            print("Invalid input. Please enter Y or N.")

#Length Check:
    
    if len(password) < 8:
        while len(password) < 8:
            password = input("This password may be too weak as it is not greater than or equal to 8 characters. If you would like to use this password, type it again, or type in a new password.")
    
#Common Passwords Check:

    common_passwords = ['password', '12345678', 'password123', 'admin123', 'welcome123', 'abc123']
    while password.casefold() in [pword.casefold() for pword in common_passwords]:
        password = input("This is a very common password. Please enter a stronger and less common password: ")

#Account Name in Passwords Check:

    while password == account or password == dictionary[account]:
        password = input("This password is the same as the account or an account in the database. Perhaps try entering another password to just type this password again to continue.")

#Sequential Characters:

    seq_char = ['123', 'abc', 'qwerty', 'asdf']
    while True:
        found = False
        for i in seq_char:
            if i in password.casefold():
                found = True
                confirm2 = input("This password contains some common sequences. Are you sure to proceed? ")
                if confirm2 in ('Yes', 'yes'):
                    break
                elif confirm2 in ('No', 'no'):
                    password = input("Please type a new password: ")
                    break
        if not found:
            break
    


while True:
    task = input("Would you like to 'Add an account' (enter A), 'Retrieve a password' (enter B), 'List all accounts' (enter C), 'Delete an account' (enter D), 'Change password' (enter E) or 'Quit'? (enter F): ")

#Task A:

    if task == 'A':
        new_acc = input("Please enter the name of your new account: ")
        if new_acc in account_and_password:
            print("This account is already in your dictionary.")
        else:
            new_pass = input("Please enter the password of your new account: ")
            password_check(new_pass, account_and_password, new_acc)

#Task B:
            
    elif task == 'B':
        repass = input("Please enter the account name: ")
        if repass in account_and_password:
            print(f"Here is your password for this account: {account_and_password[repass]}")
        else:
            print("That account is not in my database.")

#Task C:
            
    elif task == 'C':
        for i in account_and_password.keys():
            print(i)

#Task D:
            
    elif task == 'D':
        delacc = input("What account would you like to delete? ")
        if delacc in account_and_password:
            del account_and_password[delacc]
            print("Account deletion successful")
        else:
            print("That account is not in my database")

#Task E:
            
    elif task == 'E':
        edacc = input("Enter the name of the account whose password you wish to change: ")
        if edacc in account_and_password.keys():
            edpass = input("Enter a new password: ")
            if edpass in account_and_password.values():
                password_check(edpass, account_and_password, edacc)
            else:
                edpass = account_and_password[edacc]
                print("Password has been altered successfully.")
        else:
            print("This account is not in my database.")

#Task F:

    elif task == 'F':
        sys.exit()

#Exit:
        
    else:
        print("Invalid response.")
