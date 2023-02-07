# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:55:06 2022

@author: jonge
"""

from primes_and_squares import squares_generator, primes_generator

evens = set(range(0,50,2))
odds = set(range(1,50,2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.difference(primes))
print(odds - primes) # difference operator
print(primes - odds) # different

#%%
print(primes)
print(odds)
print(primes - odds)

#%%
a = {1, 2, 3, 4, 5}
b = {2,3,6}
print(a - b)