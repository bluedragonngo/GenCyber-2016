
"""

Megan Ngo
Created on Mon Jul 11 09:52:41 2016
GenCyber 2016
INTRO TO HASHING
-------

"""
#add the hash library
import hashlib

#begin defining your md5 hash
def md5(fname):
    #prepare your hash
    hash_md5 = hashlib.md5()
    #open file
    with open(fname, "rb") as f:\
        #for each 4096 byte chunk of the file
        for chunk in iter(lambda: f.read(4096), b""):
            #we are going to hash it
            hash_md5.update(chunk)
    #Gives us the hash    
    return hash_md5.hexdigest()
print(md5("/home/student/Desktop/facebook_is_lame.jpg"))
print(md5("/home/student/Desktop/looking_fresh.jpg"))
print(md5("/home/student/Desktop/myspace_profile_pic.jpg"))
print(md5("/home/student/Desktop/my_speech.jpg"))
print(md5("/home/student/Desktop/ocean_breeze.jpg"))
print(md5("/home/student/Desktop/throwback.jpg"))
print(md5("/home/student/Desktop/whitest_shirt_ever.jpg"))
print(md5("/home/student/Desktop/wishing_to_shave.jpg"))