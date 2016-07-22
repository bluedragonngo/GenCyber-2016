
"""
Megan Ngo
Created on Fri Jul  8 09:13:51 2016
GenCyber 2016
INDEXING STRINGS
----------------
"""

#use the [] to index the placement of the letter you would want to print


my_string = "pokemon go is addicting"

print(my_string[8])

#print(my_string[8:13])
seg = my_string[8:13]

print(seg)
#prints from placement 8 to the end
print(my_string[8:])
#prints from the beginning to placement 13
print(my_string[:13])

#prints backwards, so the last letter gets the -1 placement
print(my_string[-11:])