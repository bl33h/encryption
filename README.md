# encryption
A program for message encryption and decryption using the RSA algorithm. It allows users to encrypt and decrypt messages by providing prime numbers and a public key. The script utilizes modular arithmetic to perform the encryption and decryption operations.

<p align="center">
  <br>
  <img src="https://thumbs.gfycat.com/IllWelcomeGull-size_restricted.gif" alt="pic" width="500">
  <br>
</p>
<p align="center" >
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Files

- src: the file that implements de solution.

## Features
The main features of the application include:
- Message Encryption: The program allows users to encrypt messages by providing three prime numbers (p, q, and e) as input. It performs the encryption using the RSA algorithm and generates an encrypted message.
- Message Decryption: Users can decrypt encrypted messages by providing the same prime numbers (p, q, and e) used for encryption. The program uses modular arithmetic to decrypt the message and displays the original decrypted text.
- User Interaction: The program presents a menu-based interface that allows users to choose between encryption and decryption options. It prompts users for input, such as prime numbers and messages, to perform the desired operation.
- Secure Encryption Algorithm: The script utilizes the RSA encryption algorithm, which is a widely-used public-key encryption method known for its security. It ensures that the encrypted messages can only be decrypted using the corresponding private key.
- Input Validation: The program validates user input to ensure that the provided prime numbers are correct and appropriate for encryption and decryption operations.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

...
```bash
# Clone this repository
$ git clone https://github.com/bl33h/encryption

# Open the folder
$ cd src

# Run the app
$ python encryption.py

```
