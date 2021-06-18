# PM- Password Manager
## `pm` : A simple CLI for managing passwords

Have important passwords to store? Use pmcli to encrypt your passwords into files and decrypt them whenever you want!

## Install

```
pip3 install pmcli 
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
  info      Information about PMCLI
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
pm encrypt {password} {note(optional)}
```

For example:

```
pm encrypt 'Welcome982' -n google
```
Here the password `Welcome982` will be stored in encrypted format and stored in your device.

In the above example, 'google' is an ID that gives the encrypted data and identity.

You can even use `--note` instead of `-n` to add an ID

Giving an ID is completely optional, but highly recommended for every user. This helps you decrypt your messages easily

##### Decryption

There are two methods of decrypting/obtaining your passwords

###### SPECIFIC DECRYPTION

```
pm decrypt -n {note}
```

For example:

```
pm decrypt -n google
```

This gives you the stored password identified by `google` NOTE/ID.

###### MASS DECRYPTION

```
pm decryptf 
```

This gives you all of your stored passwords

```
pm decryptf
```

**NOTE: EVERY DECRYPTION METHOD NEEDS YOUT PM PASSWORD, HENCE IF YOU HAVE NOT SETUP YOUR PM, DECRYPTION WONT WORK**

##### CLEAR

`pm clear` cleans the data from data file

## Release Notes

- **Current Release- 0.2.4 (Major Update)**

### What's new?

- Double Encryption makes passwords safe and secure!
- A beautiful TUI applied
- Faster Performance
- The Files are encrypted, and stored in your device, hence it's so secure that even you can't access them without pm

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

This repository is licensed under the MIT license. See [LICENSE](https://github.com/arghyagod-coder/lola/master/LICENSE) for details.

## Special Notes

- Contribution is appreciated! Visit the contribution guide in [Contribution Guide](CONTRIBUTING.md)
- If you see anything uncomfortable or not working, file an issue in [the issue page](https://github.com/arghyagod-coder/lola/issues). Issues aren't ignored by the developers
- Thanks for seeing my project!