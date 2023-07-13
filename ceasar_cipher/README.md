# Caesar Cipher
A script that encripts a message by shifting the characters n steps using the ASCII code.It also deciphers a ciphered message by shifting the characters in reverse order.

## Algorithm
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
