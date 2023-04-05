# A `Getter` is a method used to retrieve the value of a [class] data attribute
#print(jon.get_name) # returns value of corresponding variable (or more)

# A `Setter` is a method used to define the value of the class data attribute
#jon.set_lives(300)

from player import Player
from enemy import Enemy, Troll

if __name__ == '__main__':

    #jon = Player("Jon")

    random_monster = Enemy("Basic Enemy", 12, 1)
    print(random_monster)

    random_monster.take_damage(4)
    print(random_monster)

    random_monster.take_damage(9)
    print(random_monster)

    random_monster.take_damage(9) # negative lives now ... which could be fixed
    print(random_monster)

    # Using object constructors to create troll enemies
    print()
    troll1 = Troll("Pug")
    print(troll1)

    troll2 = Troll("Erg")
    print(troll2)

    troll3 = Troll("Urg")
    print(troll3)

    troll3.grunt()
    troll2.grunt()
    troll1.grunt()

    #monster = Enemy("Basic enemy")
    #monster.grunt() # fails because no grunt() method, only trolls have it.