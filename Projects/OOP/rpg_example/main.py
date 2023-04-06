# A `Getter` is a method used to retrieve the value of a [class] data attribute
#print(jon.get_name) # returns value of corresponding variable (or more)

# A `Setter` is a method used to define the value of the class data attribute
#jon.set_lives(300)

from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing
import random

if __name__ == '__main__':
    # Polymorphism (mulitple versions/forms) uses single method that can handle multiple (arbitrary) input parameter types
    # Overloading allows one of multiple methods to be selected by examining the types of input parameters
    
    # (ex) in static languages like C or Java, one function/method may have different versions
    # -> to deal with different input arguements
    # -> print performs differently when its provided a int, float, tupple, or string.
    
    a = 3
    b = "time"
    c = 1, 2, 3 # tupple

    print(a)
    print(b)
    print(c)
    