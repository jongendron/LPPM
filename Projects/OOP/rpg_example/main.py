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
    enemy_troll = Troll() # inherits default arguements for Enemy superclass
    print(enemy_troll)

    #ugly_troll = Troll("Ugly Troll", 12, 3) # pass arguements to fullfil parameters of the Enemy superclass
    #print(ugly_troll)

    #bro_troll = Troll("Urg", 23) # no overloaded methods in python
    #print(bro_troll)