import cryptocode
import click
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

@click.group()
@click.version_option('0.1.2')
def main():
    """PM: Encrypt, decrypt and save your passwords"""
    pass

@main.command('encrypt', help='"pmcli encrypt" asks for your directory and file to save, then saves your encrypted password')
@click.argument('text', nargs=1)
def encrypt(text):
    cce = getTranslatedMessage('e', text, 13)   
    msg = cryptocode.encrypt(cce, "abcd")
    dire = input('Enter directory and file name: ')
    file = open(dire, 'w')
    file.write(msg)

@main.command('decrypt', help='"pmcli decrypt" asks for your directory and file where the password was saved an decrypts it')
def decrypt():
    dire = input('Enter directory and file name: ')
    a = open(dire)
    b = a.read()
    dmsg = cryptocode.decrypt(b, 'abcd')
    ccd = getTranslatedMessage('d', dmsg, 13) 
    print(ccd)
if __name__ == "__main__":
    main()