import cryptocode
from caesar_cypher import getTranslatedMessage
import click
@click.group()
@click.version_option('0.2.1')
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