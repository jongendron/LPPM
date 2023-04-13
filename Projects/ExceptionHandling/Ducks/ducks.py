# If object has necessary attributes, than it can be used as arguement for function even if different class.
# https://en.wikipedia.org/wiki/Duck_test

#https://www.python.org/dev/peps/pep-0484 # -> Non-goals -> The meaning of annotations

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

class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None: # parameter annotation (: type) and returns (-> type) - both are type hints!
        #if type(duck) is Duck: # DO NOT DO THIS, it prevents subclasses from being used!
        #if isinstance(duck, Duck): # checks if object is an instance of a class (Works for superclasses as well!), but not Pythonic because doesn't focus on behavior
        
        # Best to check the behavior of object rather than class (More Pythonic)
        # 1st check that the arguement duck has an attribute "fly"
        #fly_method = getattr(duck, 'fly', None) # Checks object's dictionary to see if it contains attribute specified and returns that method. Return None if it doesn't exist (instead of error).
        # fly_method = getattr(duck, 'fly') # Raises error
        fly_method = getattr(duck, 'fly', None) # Checks object's dictionary to see if it contains attribute specified and returns that method. Return None if it doesn't exist (instead of error).
        
        # 2nd check that "fly" is a method and not a data attribute (variable)
        if callable(fly_method): # checks if you can call the attribute (aka its a method). Data attributes are generally not callable.
            self.flock.append(duck)
        else:
            #raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__)) # Type Error is good choice b/c the obect type is limiting behavior.            
            raise TypeError("'" + str(type(duck).__name__) + "' class does not have method 'fly'")
        
    def migrate(self):
        problem = None
        for duck in self.flock:            
            try:
                duck.fly()
            # except AttributeError: # if one of the "duck" instances does not have the necessary attribute (.fly()) it will throw an AttributeError (Penguins in this case)
            except AttributeError as _e: # stores a reference to the exception as a variable
                #pass # pass over this "duck" in the flock
                print("One duck down")
                #raise # reraiases the exception/error caught. Useful for debugging!
                problem = _e # save exception reference to problem object
        if problem:
            raise problem # raise the error that was recognized in the try block


if __name__ == '__main__':
    donald = Duck()
    donald.fly() # calls on donald._wing attribute's method fly() (donald._wing.fly())
 

