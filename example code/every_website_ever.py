'''
    CS5001
    Spring 2019
    Sample code -- Every website ever
'''

from encryption import *
from menu import get_valid_choice
from os import path

MENU_OPTIONS = {'R':'Register', 'L':'Login', 'Q':'Quit'}
ENCRYPT_SHIFT = 5
PASSWORD_FILE = 'accounts.txt'

def write_account(username, pwd, filename):
    ''' Function write_account
        Params: user name, pwd, filename (all strings)
        Returns: True if successful, false otherwsie
    '''
    try:
        outfile = open(filename, 'a')
        outfile.write(username + ' ' + pwd + '\n')
        outfile.close()
        return True
    except OSError:
        return False
        
def read_accounts(filename):
    ''' Function read_accounts
        Params: filename, a string
        Returns: dictionary of username:password (strings)
    '''
    try:
        infile = open(filename, 'r')
        all_data = infile.read()
        lines = all_data.splitlines()
        accounts = {}
        for line in lines:
            account_list = line.split(' ')
            accounts[account_list[0]] = account_list[1]
        infile.close()
        return accounts
    except OSError:
        return {}
        
def register():
    ''' Function: register                                                      
        Parameters: none                                                        
        Returns: nothing                                                        
        Does: prompts user for username and password.                           
              validates that password is acceptable, reprompts                  
              user until they enter a good one.                                  
    '''
    username = input('\nChoose a username\n')
    pwd = input('Choose a password\n')
    encrypted_pwd = encrypt(pwd, ENCRYPT_SHIFT)
    print('I encrypted your password, now it\'s', encrypted_pwd, '\n')
    write_account(username, encrypted_pwd, PASSWORD_FILE)


def login():
    ''' Function: login                                                          
        Parameters: none                                                         
        Returns: boolean, True if login was successful, False otherwise          
                                                                                 
        Does: Prompts user for username and password. If there is no             
              account with that combination, return false, otherwise true.       
    '''
    username = input('\nEnter your username to login\n')
    pwd = input('Enter your password\n')
    encrypted_pwd = encrypt(pwd, ENCRYPT_SHIFT)

    accounts = read_accounts(PASSWORD_FILE)

    if username in accounts and accounts[username] == encrypted_pwd:
        return True

    return False


def main():

    # Prompt the user to enter an option                                         
    # Execute the option, print menu again until they quit.                      
    while True:
        user_choice = get_valid_choice(MENU_OPTIONS)

        if user_choice == 'R':
            register()
        elif user_choice == 'L':
            if login():
                print('You successfully logged in! Here is the banking '
                      'info of everyone you every met! $$$$\n')
            else:
                print('Login fail. Typed your password wrong?\n')
        elif user_choice == 'Q':
            break

    print('Thanks for using our site, I swear we won\'t tell anyone '
          'your password.')
    print('***makes shifty eyes***')

main()
