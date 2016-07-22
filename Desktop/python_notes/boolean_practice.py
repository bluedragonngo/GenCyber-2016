'''
Megan Ngo 
Created on Tue Jul  5 15:04:08 2016
GenCyber 2016
BOOLEAN PRACTICE
----------------
'''

# if - the first condition
# else - the "catch all" 
# elif - "else if", unless this happens


#AHHH THIS WORKS - takes an integer and prints even or odd
#a = int(input("Please give me a number "))
#
#def oddnumber(a):
#    if (a%2==1):
#        print("odd")
#    else: (also can be elif a%2==0)
#        print("even")      
#oddnumber(a) ---->>> CALLS THE FUNCTION


#takes an integer and prints "big or "small" if its bigger than 100
#a = int(input("Please give me a number "))
#
#def sizeofnumber(a):
#    if (a>100):
#        print("big")
#    else:
#        print("small")
#sizeofnumber(a)


#takes an integer and prints "big/small" or "even/odd"
a = int(input("Please give me a number "))
def even_odd_small_big(a):
    if (a%2==1) and (a>100):
        print("and bigger than 100 and is odd")
    elif (a%2==1) and (a<100):
        print("the number is odd and smaller than 100") 
    elif(a%2==0) and (a>100):
        print("the number is even and bigger than 100")
    else:
        print("the number is smaller than 100 and even")
even_odd_small_big(a)
