# Python is Dynamically typed Language (not static).
# It is concerned with how objects behave, rather than the type of object.
# If object has necessary attributes, than it can be used as arguement for function even if different class.
# https://en.wikipedia.org/wiki/Duck_test

# Example: when calling the print(<object>) function, any object can be passed as long as it has a __str__ method (which all do by default because of the object metaclass)
# -> This is therefor polymorphism!

# Composition is when you build a parent class using other classes to define its attributes
# For example Ducks are composed of Wings in the example below.

class Wing(object):
    """Wing Class"""
    
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        """Fly method"""
        if self.ratio > 1:
            print("Weee, this is fun!")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying.")
        else:
            print("I think I'll just walk ...")


class Duck(object):
    """Duck class"""

    def __init__(self):
        self._wing = Wing(1.8) # Creates attribute that is an instance of the class Wing.

    def walk(self):
        print("Waddle, waddle, waddle.")

    def swim(self):
        print("Come on in, the water is lovely.")

    def quack(self):
        print("Quack, quack!")

    def fly(self):
        self._wing.fly() # calls on a method in the Wing class instance (_wing).

class Penguin(object):
    """Penguin Class"""

    def walk(self):
        print("Waddle, waddle, I waddle too.")

    def swim(self):
        print("Come on i, but it's a bit chilly this far South.")

    def quack(self):
        print("Are you having a laugh? I'm a penguin!")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly() # calls on donald._wing attribute's method fly() (donald._wing.fly())
 
