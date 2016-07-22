'''
Megan Ngo
Created on Thu Jul  7 09:57:39 2016
GenCyber 2016
LOOPS IN PYTHON
---------------

WHILE loop - a conditional loop will only stop running until that 
condition is met

library - collection of code you can use
e.g. random gives you random numbers (1-100)
import random
random.randint(0,100)

'''
#mynumber = 465 #type of counter

#while mynumber>400:
#    #edit my "counter"
#    mynumber = mynumber-5
#    #mynumber-=5
#    print(mynumber)
    
''' 
import random

guess = int(input("Guess my number between (1-100) "))
number = random.randint(0,100)

while guess!=number:
    if number>guess:
        print("this number is too small ")
    else:
        print("this number is too big ")
    guess = int(input("Guess again "))
    
print("congrats, it's correct! ")
'''

#Prompt: Guess the password 
#Write a while loop that checks if a string (called password) is the
#same as the guessed password
'''
guess_pass = input("Please guess my password, all caps and 4 letters: ")
my_pass = "POOP"

while guess_pass!=my_pass:
    print("sorry thats wrong ")
    guess_pass = input("please try again ")
print("good job!")

'''

'''
#FOR LOOP 
e.g. 
for i in range(1,11,2): #i is a variable tht exists in my forloop
    print(i)

string = "Do you wanna be my lover"
for char in string: #goes through each character in the string
    print(char)
    
for i in range(10):
    print (i)

'''


'''
def ascii_to_eight_bit(letter):
    num = ord(letter)
    bitstring  = ""
    for i in range(8):
        print (num)
        if num%2 == 0:
            bitstring = "0"+bitstring
            print('0')
        else:
            bitstring = '1'+bitstring
            print('1')
        num = num//2
    return bitstring
    
print(ascii_to_eight_bit('s'))

'''

#puts in a password and tells you if it meets the requirments


password = input("Please give enter your password --->> ")

def passwordchecker(password):
    lowercase = False
    uppercase = False
    length = False

    if len(password)<6:
        print("your password is too short")
    else:
        print("correct length")  
        length = True
    
    for char in password:
       if ord(char)>96 and ord(char)<123:
          lowercase = True
       if ord(char)>64 and ord(char)<91:
          uppercase = True 
    
    if lowercase == True and uppercase == True and length == True:
        print("good to go!")
        
    elif lowercase == False:
        print("need a lowercase")
        
    elif uppercase == False:
        print("need an uppercase")
        
    else:
        print("Sorry, you need a new password")
        
passwordchecker(password)
     






































