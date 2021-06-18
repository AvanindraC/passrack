'''
Password Manager- 0.2.0

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


import cryptocode
import click
import os
import pickle

# MAIN ENCRYPTION LOGIC

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
MAX_KEY_SIZE = len(SYMBOLS)
def getKey():
    key = 0
    while True:
        key = 13
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

@click.group()
@click.version_option('0.2.0')
def main():
    """PM: Encrypt, decrypt and save your passwords"""
    pass

'''
================================================================================================
================================================================================================
'''

# ENCRYPTION LOGIC

@main.command('encrypt', help='Encrypt your message')
@click.argument('directory', nargs=1)
@click.argument('content', nargs=1)
@click.option('--note', nargs=1)
def encrypt(content, directory, note):
    try:
        cce = getTranslatedMessage('e', content, 13)   
        msg = cryptocode.encrypt(cce, "abcd")
        if directory!='current':
            os.chdir(directory)
        file = open('.data_encr.dat', 'a')
        file.write((msg+f'------------------ {note}'+'\n'))
    except FileNotFoundError:
        print("The directory doesn't exist")
    

'''
================================================================================================
================================================================================================
'''

# SPECIFIC DECRYPTION LOGIC
@main.command('decrypt', help='Decrypt any of your passwords')
@click.argument('directory', nargs=1)
@click.option('--note', '-n', nargs=1)
def decrypt(note, directory):
    inp = click.prompt('Enter your password')
    ops = pickle.load(open('.pmcli.dat', 'rb'))
    ops = cryptocode.decrypt(ops, "abcd")
    if inp==ops:
        if note==None:
            note=''
        try:
            if directory!='current':
                os.chdir(directory)
            a = open('.data_encr.dat', 'r')
            b = a.readlines()
            res=0
            for line in b:
                if note in line:
                    line= line.replace('------------------ {note}', '')
                    line =line.replace('\n', '')
                    c = line
                    dmsg = cryptocode.decrypt(c, 'abcd')
                    ccd = getTranslatedMessage('d', dmsg, 13) 
                    print(ccd)
                    break
                else:
                    res+=1
            
        except FileNotFoundError:
            print("The directory or file doesn't exist")
        if res==(len(b)):
            print('Invalid Identity Key')

    else:
        print('Invalid Password')

'''
================================================================================================
================================================================================================
'''

# Mass DECRYPTION LOGIC

@main.command('decryptf', help='Decrypt all your passwords')
@click.argument('directory', nargs=1)
def decrypt(directory):
    inp = click.prompt('Enter your password: ')
    ops = pickle.load(open('.pmcli.dat', 'rb'))
    ops = cryptocode.decrypt(ops, "abcd")
    if inp==ops:
        try:
            if directory!='current':
                os.chdir(directory)
            a = open('.data_encr.dat', 'r')
            b = a.readlines()
            cd=[]
            for line in b:
                cd.append(line)

            for c in cd:   
                dmsg = cryptocode.decrypt(c, 'abcd')
                ccd = getTranslatedMessage('d', dmsg, 13) 
                print(ccd)
        except FileNotFoundError:
            print("The directory or file doesn't exist")
    else:
        print('Invalid Password')

'''
================================================================================================
================================================================================================
'''

# CLEAR COMMAND

@main.command(help='Clear existing data')
@click.argument('directory', nargs=1)
def clear(directory):
    if directory!='current':
        os.chdir(directory)
    a = open('.data_encr.dat', 'w')
    b = a.write('')

'''
================================================================================================
================================================================================================
'''

# SETUP COMMANDS

@main.command('init', help='Initialize pmcli for you to get started with it')
def init():
    defps = 'fetcher'
    defps = cryptocode.encrypt(defps, "abcd")
    pickle.dump(defps, open('.pmcli.dat', 'wb'))

@main.command('config', help='Set your configuration for pm')
@click.option('--password', '-ps')
def config(password):
    inp = click.prompt('Enter your old password: ', confirmation_prompt=True)
    ops = pickle.load(open('.pmcli.dat', 'rb'))
    ops = cryptocode.decrypt(ops, "abcd")
    if inp==ops:
        password= cryptocode.encrypt(password, "abcd")
        pickle.dump(password, open('.pmcli.dat', 'wb'))
    else:
        click.echo('Access Denied!')


'''
================================================================================================
================================================================================================
'''

if __name__ == "__main__":
    main()