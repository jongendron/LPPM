# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:29:08 2022

@author: jonge
"""

import hashlib

# print(sorted(hashlib.algorithms_guaranteed))
# print()
# print(sorted(hashlib.algorithms_available))

#%% Create a sha256 hashlib
python_program = """for i in range(10):
    print(i)
"""
print(python_program)
print()

#%% Encode a string before feeding it to a hash function
for b in python_program.encode('utf8'):
    print(b, chr(b))
print()

original_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256: {original_hash.hexdigest()}") # hexidecimal number of 256 bit (32 bytes)
print()

python_program += "print(('code change')"
print(python_program)
print()
#print(type(original_hash)) # format is bashlib.HASH

new_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256: {new_hash.hexdigest()}")
print()

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed")
else:
    print("The code has been modified")
print()    
    
# Code often has a hash number for you to compare after you download
# to make sure it is the same