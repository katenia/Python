import re
#import stdiomask #mask user input
import sys
import time
from os import system, name

requirements = ['8 characters or more', 'at least 1 uppercase character', 'at least 1 digit', 'at least 1 special character (!, ?, @, %)']

def welcome():
    print ('A strong password contains ' + (', '.join(requirements)))
    print ('or hit enter to exit')
    getPassword()

def secondAttemp():
    print ('Would you like to try another password? Yes/No')
    again = input()
    while True:
        if again.lower() in ["yes", "y"]:
            welcome()
        elif again.lower() in ["no", "n"]:
            system('cls') #clears the screen
        else:
            print ('That is not a valid input. Please enter Yes or No')
            again = input()
            continue

def getPassword():
    print ('Enter your password:')
    pw = input ()
    if len(pw) != 0:
        if validate(pw):
            print ('Excellent. Your password is strong!')
            secondAttemp()
        else:
            time.sleep(3)
            if name == 'nt':
                system('cls') #clears the screen
            else:
                system('clear') #clears the screen on non-windows machine
            welcome()
    else:
        print ('Have a great day! Goodbye.')
        sys.exit()

def validate(pw):
    if len(pw) < 8:
        print ('Your password appears to be too short. Please wait...\n')
        return False
    elif re.search('[0-9]', pw) is None:
        print ('Your password does not appear to include a digit. Please wait...')
        return False
    elif re.search('[A-Z]',pw) is None:
        print ('Your passward appears to have no uppercase letters. Please wait...')
        return False
    elif re.search('[!|?|#|@|%]',pw) is None:
        print ('Your password appears to have no special character. Please wait...')
        print ('Include a !, ?, @, or  %')
        return False
    else:
        return True



print ('Welcome')
print ('This program will help insure your password is strong.')
welcome ()