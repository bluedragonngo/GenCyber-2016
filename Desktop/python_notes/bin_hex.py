#Megan Ngo 
#Created on Tue Jul  5 15:04:08 2016
#GenCyber 2016
#Intro to Python Exercise

# % is the remainder
# // is the quotient

#when going from hex to binary
#bin("0x" + hex,16) **you have to specify the base otherwise it is ten

hex_digit = input("Give me a hex number ")

print(bin(int("0x"+hex_digit,16)))