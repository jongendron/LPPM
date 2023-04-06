# Python is Dynamically typed Language (not static).
# It is concerned with how objects behave, rather than the type of object.
# If object has necessary attributes, than it can be used as arguement for function even if different class.
# https://en.wikipedia.org/wiki/Duck_test

# Example: when calling the print(<object>) function, any object can be passed as long as it has a __str__ method (which all do by default because of the object metaclass)
# -> This is therefor polymorphism!

class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle.")

    def swim(self):
        print("Come on in, the water is lovely.")

    def quack(self):
        print("Quack, quack!")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too.")

    def swim(self):
        print("Come on i, but it's a bit chilly this far South.")

    def quack(self):
        print("Are you having a laugh? I'm a penguin!")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin() # percy is a duck according to the test_duck method (because Python only care's about behavior rather than class)
    test_duck(percy) # Penguin and Duck classes both have walk, swim, and quack methods ... therefore test_duck assumes it passes as a duck!