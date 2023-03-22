# A `Getter` is a method used to retrieve the value of a [class] data attribute
#print(jon.get_name) # returns value of corresponding variable (or more)

# A `Setter` is a method used to define the value of the class data attribute
#jon.set_lives(300)

from player import Player

if __name__ == '__main__':

    jon = Player("Jon")

    print('Name: ', jon._name)
    print('Lives: ', jon.lives)
    jon.lives -= 1
    print(jon)
    jon.lives -= 1
    print(jon)
    jon.lives -= 1
    print(jon)
    #jon._lives = 9
    #print(jon)
    jon.level = 3
    print(jon)
    jon.level -= 3
    print(jon)