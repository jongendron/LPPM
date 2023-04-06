# A `Getter` is a method used to retrieve the value of a [class] data attribute
#print(jon.get_name) # returns value of corresponding variable (or more)

# A `Setter` is a method used to define the value of the class data attribute
#jon.set_lives(300)

from player import Player
from enemy import Enemy, Troll, Vampyre

if __name__ == '__main__':

    #jon = Player("Jon")
    vamp1 = Vampyre("Dracula")
    print(vamp1)

    vamp2 = Vampyre("Count Chocula")
    print(vamp2)

    vamp2.take_damage(6)
    print(vamp2)

    vamp2.take_damage(7)
    print(vamp2)

    troll1 = Troll("Henry")
    print(troll1)
    troll1.take_damage(30)
    print(troll1)