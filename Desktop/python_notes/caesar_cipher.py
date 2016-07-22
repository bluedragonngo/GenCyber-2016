
"""
Megan Ngo
Created on Fri Jul  8 09:42:00 2016
GenCyber 2016
INTRO INTO CAESAR CIPHER
------------------------
"""


#ANOM IS SO SMART
    
# takes a message and encrypts the message

#def caesar_cipher():
#    letter = input("please give me your message ---->>> ")
#    encrypt = ""
#    shift = 0
#    while shift<26:
#        shift = shift+1
#        
#        for char in letter:
#            
#            number = ord(char)+shift
#            if number>122:
#                number-=26
#            elif number==32+shift:
#                number=32
#            elif number>90 and number<97:
#                number-=26
#            encrypt = (encrypt+chr(number))
#    return(encrypt)
#   
#print(caesar_cipher())


#takes an encrypted message and de-codes for you
'''
def decrypt_stuff():
    encryption = input("please give me your encrypted message ---> ")
    new_message = ""
    shift = int(input('please give me your shift # ---> '))
    for char in encryption:
        number = ord(char)+shift
        if number>122:
            number-=26
        elif number==32+shift:
            number=32
        elif number>90 and number<97:
            number-=26
        new_message = (new_message+ chr(number))
    return(new_message)
   
print(decrypt_stuff())
'''

# lists the decrypted messages


def decryptCC(): #one parameter called encrypted. string var
    encrypted = input("please give me your encrypted string: ")
    for i in range(26):  # for loop that goes through numbers 0-26
        decrypted = "" #empty string every iteration of the for loop
        for char in encrypted: 
        #for loop inside for loop that loops through ea. char in string
            number = ord(char) #convert char to ascii value
            if number >= 65 and number <= 91: #check if upper
                number -= i #decrypt shift
                if number< 65: #checks if ascii value is below 65 range
                    number+= 26 #if true, add 26 to make it a letter
                decrypted += chr(number) #add the decrypted char to decrypted string
            elif number <= 122 and number>=97: #check if lower
                number -= i
                if number<97:
                    number+=26 
                decrypted +=chr(number)
            else:
                decrypted += char #adds random char (not letter) to string
        print(i, decrypted) 
        #print each different variation of CC in the first for loop
    return (True) 

decryptCC() #testing decryption 

































