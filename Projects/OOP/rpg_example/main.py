# A `Getter` is a method used to retrieve the value of a [class] data attribute
#print(jon.get_name) # returns value of corresponding variable (or more)

# A `Setter` is a method used to define the value of the class data attribute
#jon.set_lives(300)

from player import Player
from enemy import Enemy, Troll, Vampyre

if __name__ == '__main__':

    #jon = Player("Jon")
    #print(jon)
    
    #troll1 = Troll("Gronk")
    #print(troll1)
    
    vamp1 = Vampyre("Dracula")
    print(vamp1)

    #while vamp1.alive:
        #print(vamp1)
        #print("\t",end="")
        #if not vamp1.dodges():
        #vamp1.take_damage(1)

    #vamp1._lives = 0
    #vamp1._hp = 1
    #print(vamp1)

    