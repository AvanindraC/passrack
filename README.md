# PassRack- Password Manager
## `PassRack` : A simple CLI for managing passwords

Have important passwords to store? Use passrack to encrypt your passwords into files and decrypt them whenever you want!

## Install

```
pip3 install passrack 
```

## Dependencies
+ `click` 
+ `click_help_colors`
+ `pyfiglet`
+ `cryptocode`

## Built with
+ `Python 3.9.5` 

## Supported Platforms:

+ Operating System = Cross-Platform

## How to use

Open powershell for Windows or Terminal for Linux/Mac and  and type ```prack```

If this result comes, then you have successfully installed rassrack on your system

```

  PassRack: Encrypt, decrypt and save your passwords

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  clear     Clear existing data
  config    Set your configuration for PassRack
  decrypt   Decrypt any of your passwords
  decryptf  Decrypt all your passwords
  encrypt   Encrypt your message
  info      Information about PassRack
  init      Initialize passrack for you to get started with it
  suggest   Get a password suggestion
```

else, try the above steps again!

#### Setup

First you need to setup passrack for yourself

Procedure:

- Run `prack init` to initialize prack for your directory

There should be no output

- Run `prack config -ps <password>` to set your password for prack. It will ask you for your OLD PASSWORD
  - Now if you haven't configured your passowrd before, enter `fetcher` in the OLD PASSWORD INPUT which is the default password

**NOTE: THIS STORES YOUR PASSWORD FOR PASSRACK AND DOES NOT INDICATE A PASSWORD FOR PASSWORD MANAGEMENT**

- Now you are set up to use passrack

##### Encryption:

```
prack encrypt {password} {note(optional)}
```

For example:

```
prack encrypt 'Welcome982' -n google
```
Here the password `Welcome982` will be stored in encrypted format and stored in your device.

In the above example, 'google' is an ID that gives the encrypted data and identity.

You can even use `--note` instead of `-n` to add an ID

Giving an ID is completely optional, but highly recommended for every user. This helps you decrypt your messages easily

##### Decryption

There are two methods of decrypting/obtaining your passwords

###### SPECIFIC DECRYPTION

```
prack decrypt -n {note}
```

For example:

```
prack decrypt -n google
```

This gives you the stored password identified by `google` NOTE/ID.

###### MASS DECRYPTION

```
prack decryptf 
```

This gives you all of your stored passwords

```
prack decryptf
```

##### SUGGEST

```
prack suggest -n google
```

This gives a strong password suggestion, also gives you an option to save the password in pm with identifier note.

**NOTE: EVERY DECRYPTION METHOD NEEDS YOUR PassRack PASSWORD, HENCE IF YOU HAVE NOT SETUP PASSRACK, DECRYPTION WONT WORK**

##### CLEAR

`prack clear` cleans the data from data file

## Release Notes

- **Current Release- 0.2.4 (Major Update)**

### What's new?

- Double Encryption makes passwords safe and secure!
- A beautiful TUI applied
- Faster Performance
- The Files are encrypted, and stored in your device, hence it's so secure that even you can't access them without prack
- Added Password Suggestion

#### Developers
- [Avanindra Chakraborty](https://github.com/AvanindraC)
- [Arghya Sarkar](https://github.com/arghyagod-coder)
- [Shravan Asati](https://github.com/Shravan-1908)


### Developer Tools

- [Visual Studio Code](https://github.com/microsoft/vscode)

- [Python 3.9.5](https://python.org)

- [Git](https://git-scm.com)

- [Python Poetry](https://python-poetry.org/)

## License

License © 2021-Present Avanindra Chakraborty

This repository is licensed under the MIT license. See [LICENSE](https://github.com/AvanindraC/PMCLI/blob/main/LICENSE) for details.

## Special Notes

- Contribution is appreciated! 
- If you see anything uncomfortable or not working, file an issue in [the issue page](https://github.com/AvanindraC/PMCLI/issues). Issues aren't ignored by the developers
- Thanks for seeing my project!