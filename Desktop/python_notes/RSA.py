"""
Megan Ngo
Created on Tue Jul 19 10:21:32 2016
GenCyber 2016
INTRO TO RSA
------------

"""

#takes numbers and encrypts your message in RSA
p = int(input("Give me a prime number: "))
q = int(input("and another: "))
print("      ","your n value is", p*q)
n = p*q
t = int(input("Give me your t value (not a factor of n): "))

    
for i in range(1,1000):
    i+=1
    if (6*i)%(n)==1:
        print("your value is ", i)
           
