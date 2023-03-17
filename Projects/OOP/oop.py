about_oop = """
Class: template for creating objects. All objects created using
    the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.

- In Python, every type is a class
- Classes are dynamic and can be changes after definition

Constructor: Special method that is executed when instance
    of class is created or constructed. In Python, this is "__init__".
    When you call a method of an instance, Python Automatically provides
    a reference to the instance as the first parameter to the method.

"""

# self is a reference to the instance of the class
# used to reffer to instance variables
# self can also be changed to any name, but "self" is default in __init__

# Classes are templates for making objects
class Kettle(object):

    power_source = "electricity" # class attribute

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

# kenwood is an instance of the class Kettle()
# aka kenwood is an object of type kettle()    
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print('\t', kenwood.price)

kenwood.price = 12.75
print('\t',kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make)
print('\t', hamilton.price)

print("Models:\n{} = {}\n{} = {}" \
      .format(kenwood.make, kenwood.price, \
              hamilton.make, hamilton.price))

# when a variable is bound to instance of a class then 
# its refered to as a data attribute in python
# fields in java 
# data members in c++
print("Models:\n{0.make} = {0.price}\n{1.make} = {1.price}" \
      .format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Calling the class method directly
# requires user to specify the instance
# you want to apply method to
# Kettle.switch_on() # fails because instance not specified
Kettle.switch_on(kenwood)
print(kenwood.on)

# Classes are dynamic and can be changes after definition
print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
#print(hamilton.power) # no default for power in class so error
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print()
print(Kettle.__dict__) # contains entire namespace
print()
print(kenwood.__dict__) # only contains varaible defined in instance of class
print()
print(hamilton.__dict__) # same
print()

# Therefore when the class attribute it requested by instance
# it is grabbed from the parent class, not the instance object
# therefore if you change the attr then it changs it for all instances
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print()

# If you change class attribute for a specific instance
# it will create a new local variable that shadows it
kenwood.power_source = "nuclear"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print()
print(Kettle.__dict__)
print()
print(kenwood.__dict__) # local variable for power_source assigned
print()
print(hamilton.__dict__)
print()