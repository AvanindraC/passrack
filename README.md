# PMCLI

## A password encrypter and decrypter

Have important passwords to store? Use pmcli to encrypt your passwords into files and decrypt them whenever you want!

## Install

```
pip3 install pmcli 
```

## How to use

Open powershell for Windows or Terminal for Linux/Mac and  and type ```pm```

If this result comes, then you have successfully installed pmcli on your system

```
  PM: Encrypt, decrypt and save your passwords

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  clear     Clear existing data
  config    Set your configuration for pm
  decrypt   Decrypt any of your passwords
  decryptf  Decrypt all your passwords
  encrypt   Encrypt your message
  init      Initialize pmcli for you to get started with it
```

else, try the above steps again!

#### Setup

First you need to setup pm for yourself

Procedure:

- Run `pm init` to initialize pm for your directory

There should be no output

- Run `pm config -ps <password>` to set your password for PM. It will ask you for your OLD PASSWORD
  - Now if you haven't configured your passowrd before, enter `fetcher` in the OLD PASSWORD INPUT which is the default password

**NOTE: THIS STORES YOUR PASSWORD FOR PM AND DOES NOT INDICATE A PASSWORD FOR PASSWORD MANAGEMENT**

- Now you are set up to use PM

##### Encryption:

```
pm encrypt {directory} {note(optional)}
```

For example:

```
pm encrypt C://Users//doge//Desktop//Office//files 'Welcome982' -n google
```

This makes a data_encr.dat file which consists the message 'Hello World' in the files folder located in Office folder present in your Desktop.

For using current directory, just provide `current` instead of the directory.

In the above example, 'google' is an ID that gives the encrypted data and identity.

You can even use `--note` instead of `-n` to add an ID

Giving an ID is completely optional, but highly recommended for every user. This helps you decrypt your messages easily

##### Decryption

There are two methods of decrypting/obtaining your passwords

###### SPECIFIC DECRYPTION

```
pm decrypt {directory} -n {note}
```

For example:

```
pm decrypt C://Users//arghy//Desktop//Office//files -n google
```

This gives you the stored password identified by `google` NOTE/ID.

For using current directory, just provide `current` instead of the directory.

###### MASS DECRYPTION

```
pm decrypt {directory} 
```

This gives you all of your stored passwords

```
pm decrypt C://Users//arghy//Desktop//Office//files
```

**NOTE: EVERY DECRYPTION METHOD NEEDS YOUT PM PASSWORD, HENCE IF YOU HAVE NOT SETUP YOUR PM, DECRYPTION WONT WORK**

##### CLEAR

`pm clear {directory}` cleans the data from data file

### Developer Tools

[Visual Studio Code](https://github.com/microsoft/vscode)

[Python 3.9.5](https://python.org)

[Git](https://git-scm.com)
