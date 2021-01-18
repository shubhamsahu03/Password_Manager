![Logo_Password_manager](https://user-images.githubusercontent.com/71839040/104889364-1eb2d380-5994-11eb-9e82-36aeb99b1c85.png)


# Password_Manager

Password Manager in Python using pyaes and hashlib.

## Description

Todo:
1. Create your Account by entering an Username and a master password.
2. This master password will be used for the creation of the security key,which will be used for encrypting and decrypting all of your passwords in your Account.
3. The Hashing algorithm used is sha256.
4. Your Account passwords will be encrypted in counter mode of aes encryption method.
5. Your Account table (Database used is MYSQL) has columns: Title,Username,URL,Password,Email-ID.
6. Search Your Passwords by entering the corresponding Title or Username or URL.

## Dependencies 

- pymysql
- pbkdf2 
- secrets 
- pillow 
- pyperclip
- pyaes


