'''
Password Manager- 0.2.8

--- Avanindra Chakroborty 
|-----Arghya Sarkar

- New Features:

Completely Renovated Workflow

FLOW:

1. RUN pm init TO INITIALISE YOUR PM WITH DEFAULT CONFIGURATION

2. RUN pm config -ps <password> OR pm config --password <password> TO SET YOUR OWN PASSWORD (CHANGING THE DEFAULT ONE WHICH IS FETCHER)

3. NEW ENCRYPTION COMMAND :- pm encrypt <directory> <message> <note(optional)>
----- NOTE IS LIKE AN ID TO YOUR PASSWORD. FOR EXAMPLE YOU ARE STORING A PASSWORD FOR GOOGLE ACCOUNT. USE pm encrypt <directory> <message> googleac
----- THIS ID/NOTE IS USED TO LOCATE YOUR PASSWORDS WHILE DECRYPTING IT
----- USE pm encrypt current <message> <note(optional)> TO WORK IN YOUR CURRENT DIRECTORY

4. A DATA FILE ON THE SAME LOCATION GETS CREATED WHICH IS HIDDEN. THE SINGLE DATA FILE STORES ALL PASSWORDS

5. NEW DECRYPTION COMMAND:- THERE ARE TWO DECRYPTION COMMANDS

pm decrypt <directory> -n <note> OR pm decrypt <directory> --note <note>

THE ABOVE COMMAND DECRYPTS A SPECIFIC NOTE/ID OF YOUR PASSWORD

pm decryptf <directory>

THE ABOVE COMMAND GIVES YOU THE WHOLE LIST OF SAVED PASSWORDS

6. CLEAR COMMAND: - pm clear <directory> CLEARS ALL THE STORED DATA FROM YOUR DATA FILE

7. PM IS NOW MORE SECURE AND YOUR DATA IS STORED IN A SECURE WAY SO HACKERS.... GOOD BYE :)
'''

from click import secho
import cryptocode
import click
import os
import pickle
from pyfiglet import Figlet
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from random import randint
import random
# Defining BinarytoDecimal() function
'''
================================================================================================
================================================================================================
'''
def BinaryToDecimal(binary):
      
    # Using int function to convert to
    # string   
    string = int(binary, 2)
      
    return string
      
 
'''
================================================================================================
================================================================================================
'''  
# MAIN ENCRYPTION LOGIC

'''
================================================================================================
================================================================================================
'''

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

MAX_KEY_SIZE = len(SYMBOLS)
def getKey():
    cck = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".cck.dat")), 'rb'))
    key = 0
    while True:
        key = cck
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
def getTranslatedMessage(mode,message , key):
    if mode [0] == 'd':
        key = -key
    translated = ''
            
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
                    
            translated += SYMBOLS[symbolIndex]
    return translated

'''
================================================================================================
================================================================================================
'''

# BASE COMMAND

@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan"
)
@click.version_option('0.2.8')
def main():
    """PM: Encrypt, decrypt and save your passwords"""
    pass

'''
=================================================================================================
=================================================================================================
'''

# ENCRYPTION LOGIC

@main.command('encrypt', help='Encrypt your message')
@click.argument('content', nargs=1)
def encrypt(content):
    
    cck = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".cck.dat")), 'rb'))
    cek = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".key.dat")), 'rb'))
    cce = getTranslatedMessage('e', content, cck )   
    msg = cryptocode.encrypt(cce, cek)
    resf = ''.join(format(ord(i), '08b') for i in msg)
    file = open((os.path.join(os.path.expanduser("~"), ".pmcli", ".data_encr.dat")), 'a')
    file.write((resf+'\n'))

    

'''
================================================================================================
================================================================================================
'''

# SPECIFIC DECRYPTION LOGIC
@main.command('decrypt', help='Decrypt any of your passwords')
def decrypt():
    
    cck = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".cck.dat")), 'rb'))
    cek = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".key.dat")), 'rb'))
    inp = click.prompt(click.style('Enter your password', fg='blue'), confirmation_prompt=True)
    ops = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".pmcli.dat")), 'rb'))
    ops = cryptocode.decrypt(ops, cek)
    if inp==ops:
        a = open((os.path.join(os.path.expanduser("~"), ".pmcli", ".data_encr.dat")), 'r')
        b = a.readlines()
        res=0
        for line in b:
            line =line.replace('\n', '')
            c = line
            bin_data = c
            str_data =' '
   
            for i in range(0, len(bin_data), 7):
      

                temp_data = bin_data[i:i + 7]

                decimal_data = BinaryToDecimal(temp_data)
       
                str_data = str_data + chr(decimal_data)
            dmsg = cryptocode.decrypt(str_data, cek)
            ccd = getTranslatedMessage('d', dmsg, cck) 
            click.clear()
            secho(ccd, fg='blue', bg= 'black')
            break
        else:
            res+=1
        if res==(len(b)):
            secho('Invalid Identity Key', fg='red', bg= 'black')

    else:
        click.secho('Invalid Password', fg='red', bg= 'black')

'''
================================================================================================
================================================================================================
'''

# Mass DECRYPTION LOGIC

@main.command('decryptf', help='Decrypt all your passwords')
def decryptf():
    
    cck = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".cck.dat")), 'rb'))
    cek = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".key.dat")), 'rb'))
    inp = click.prompt(click.style('Enter your password', fg='blue'), confirmation_prompt=True)
    ops = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".pmcli.dat")), 'rb'))
    ops = cryptocode.decrypt(ops, cek)
    if inp==ops:
        a = open((os.path.join(os.path.expanduser("~"), ".pmcli", ".data_encr.dat")), 'r')
        b = a.readlines()
        cd=[]
        for line in b:
            cd.append(line)
        for c in cd:   

            c = line
            bin_data = c
            str_data =' '
   
            for i in range(0, len(bin_data), 7):
      

                temp_data = bin_data[i:i + 7]

                decimal_data = BinaryToDecimal(temp_data)
       
                str_data = str_data + chr(decimal_data)
            dmsg = cryptocode.decrypt(str_data, cek)
            ccd = getTranslatedMessage('d', dmsg, cck) 
            click.clear()
            secho(ccd, fg='blue', bg= 'black')
    else:
        secho('Invalid Password', fg='red', bg= 'black')

'''
================================================================================================
================================================================================================
'''

# CLEAR COMMAND

@main.command(help='Clear existing data')
def clear():
    a = open((os.path.join(os.path.expanduser("~"), ".pmcli", ".data_encr.dat")), 'w')
    b = a.write('')

'''
================================================================================================
================================================================================================
'''

# SETUP COMMANDS

@main.command('init', help='Initialize pmcli for you to get started with it')
def init():
    try:
        os.mkdir((os.path.join(os.path.expanduser("~"), ".pmcli")))
        defps = 'fetcher'
        key = random.choice(SYMBOLS)
        pickle.dump(key, open((os.path.join(os.path.expanduser("~"), ".pmcli", ".key.dat")), 'wb'))
        key = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".key.dat")), 'rb'))
        defps = cryptocode.encrypt(defps, key)
        pickle.dump(defps, open((os.path.join(os.path.expanduser("~"), ".pmcli", ".pmcli.dat")), 'wb'))
        cck = randint(1,25)
        pickle.dump(cck, open((os.path.join(os.path.expanduser("~"), ".pmcli", ".cck.dat")), 'wb'))
    except FileExistsError as e:
        print('File already exists')
@main.command('config', help='Set your configuration for pm')
@click.option('--password', '-ps')
def config(password):
    cck = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".cck.dat")), 'rb'))
    cek = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".key.dat")), 'rb'))
    inp = click.prompt(click.style('Enter your old password', fg='blue'), confirmation_prompt=True)
    ops = pickle.load(open((os.path.join(os.path.expanduser("~"), ".pmcli", ".pmcli.dat")), 'rb'))
    ops = cryptocode.decrypt(ops, cek)
    if inp==ops:
        passcode = click.prompt(click.style('Enter new password', fg='blue'), confirmation_prompt=True)
        password= cryptocode.encrypt(passcode, cek)
        pickle.dump(password, open((os.path.join(os.path.expanduser("~"), ".pmcli", ".pmcli.dat")), 'wb'))
    else:
        click.secho('Access Denied!', fg='red', bg= 'black')


@main.command('info', help='Information about PMCLI')
def info():
    """Info About CLI """
    f = Figlet(font='standard')
    click.secho(f.renderText('PM'), fg='green')
    click.secho("pm: a simple CLI password manager",fg='cyan')
    click.secho("\n\nPasswords are meant to be safe, \n  So it's our duty to save them!",fg='cyan')
    click.secho("\n\nDeveloper: Avanindra Chakraborty", fg='green', bg= 'black')

'''
================================================================================================
================================================================================================
'''

if __name__ == "__main__":
    main()
    
