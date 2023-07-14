'''
1. create variables to hold the ciphered and deciphered messages
2. create a function(message ,steps)
3. Loop through each char in the message
   a. If char == letter ,
   shift it n steps foward in the alphabet using ord() and chr() functions
   b. If char !== letter,
   leave it as it is
   c. Append the shifted char to the variables
4.Return the ciphered message string
5.Create a function to decipher(message,steps)
3. Loop through each char in the message
   a. If char == letter ,
   shift it n steps backward in the alphabet using ord() and chr() functions
   b. If char !== letter,
   leave it as it is
   c. Append the shifted char to the variables
7. Return deciphered message
'''
import pyfiglet as pfg
from termcolor import colored

text = pfg.figlet_format('ceasar cipher',font='doom')

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
            
    print(f'ciphered message : {colored(ciphered_message,"green")}')
    return ciphered_message

def caesar_decipher(message,shift):
    return caesar_cipher(message,-shift)


def lets_cipher():
    print(colored(text,'green'))
    print("Welcome to ceasar cipher")
    reply = int(input(colored("Reply with 1 to encode and 2 to decode : ","green")))
    direction = "encode" if reply == 1 else "decode"
    message = input(f'Type in the message to {direction} : ')
    steps =  int(input("Type the shift number : "))
    if direction == "encode":
        caesar_cipher(message,steps)
    elif direction == "decode":
        caesar_decipher(message,steps)
    else:
        print("unsupported option")

lets_cipher()