"""

Megan Ngo
Created on Fri Jul  8 13:38:35 2016
GenCyber 2016
Intro to ONE TIME PAD
---------------------

"""
#onetimepad is when the shift is completely random for each character

def onetimepad(text,pad):
    convertedText = ''
    i=0
    for letter in text:
        convertedText+=chr(ord(pad[i]^ord(text[1])))
        i= i + 1
        if i > len(text):
            break
    return convertedText

pad = input('Enter the secret pad. This is shared between sender and receiver')

