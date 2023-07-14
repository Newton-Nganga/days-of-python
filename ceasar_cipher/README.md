# Caesar Cipher
A script that encripts a message by shifting the characters n steps using the ASCII code.It also deciphers a ciphered message by shifting the characters in reverse order.

## Dependencies  
- pyfiglet  
- termcolor  
  
##  Base Algorithm

The ciphering script  
```python
...
def caesar_cipher(message,shift):
    ciphered_message  = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphered_message += shifted_char
        else:
            #preserve non alphabets
            ciphered_message += char
            
    print(f'ciphered message : {ciphered_message}')
    return ciphered_message
...
```
The deciphering Script  
```python
def caesar_decipher(message,shift):
    return caesar_cipher(message,-shift)
```
## Running the program
 Clone this repo
 ```sh
    git clone https://github.com/Newton-Nganga/days-of-python.git
 ```
 mOve into the ceaser_cipher directory and run the pyhton script
 ```sh
    cd days-of-python/ceasar_cipher && python3 script.py
 ```
## The view of the Program
```sh
                                      _       _               
                                     (_)     | |              
  ___ ___  __ _ ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __ 
 / __/ _ \/ _` / __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_|  __/ (_| \__ \ (_| | |    | (__| | |_) | | | |  __/ |   
 \___\___|\__,_|___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                       | |                    
                                       |_|                    

Welcome to ceasar cipher
Reply with 1 to encode and 2 to decode : 1
Type in the message to encode : To day must have been a great day.
Type the shift number : 7
ciphered message : Av khf tbza ohcl illu h nylha khf.

```
