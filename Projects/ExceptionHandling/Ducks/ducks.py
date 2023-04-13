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


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None: # parameter annotation (: type) and returns (-> type) - both are type hints!
        self.flock.append(duck)

    def migrate(self):
        for duck in self.flock:
            problem = None
            try:
                duck.fly()
            # except AttributeError: # if one of the "duck" instances does not have the necessary attribute (.fly()) it will throw an AttributeError (Penguins in this case)
            except AttributeError as e: # stores a reference to the exception as a variable
                #pass # pass over this "duck" in the flock
                print("One duck down")
                #raise # reraiases the exception/error caught. Useful for debugging!
                problem = e # save exception reference to problem object
        if problem:
            raise problem # raise the error that was recognized in the try block


if __name__ == '__main__':
    donald = Duck()
    donald.fly() # calls on donald._wing attribute's method fly() (donald._wing.fly())
 

