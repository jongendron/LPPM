# use regular expressions (regex) to find all digits followed by a "." and add a _ at the end
# search: (\{\d\.)
# replace: $1_
import random


#class Enemy:
class Enemy(object): # inherit object superclass (same as above but more verbose, but only in Python 3)
    """Highest superclass of enemies (aside from object class)."""

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hp = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage, maxhp=12): # TODO: is there a way to replace 30 with the maxhp for a subclass?
        remaining_points = self._hp - damage
        if remaining_points >= 0:
            self._hp = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hp))
        else: 
            self._lives -= 1
            if self._lives > 0:                            
                self._hp = maxhp
                print(f"{self._name} lost a life.")
            else:
                self._hp = 0
                self._alive = False
                print(f"{self._name} has died.") # enemy died (lost a life)

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hitpoints: {0._hp}".format(self) # replacement fields aren't changed during refactoring -> rename methods


class Troll(Enemy):  # 1st parameter is a superclass to inherit
    """Troll subclass of Enemy."""

    def __init__(self, name="Enemy Troll"): # current class constructor (this call cancels the superclass's constructor)
        #Enemy.__init__(self, name=name, lives=1, hit_points=23) # Python 2: calls on Enemy superclass's constructor (__init__()) as part of Troll()'s __init__()
        #super(Troll, self).__init__(name=name, lives=1, hit_points=23) # Python 3 way
        super().__init__(name=name, lives=1, hit_points=23) # Compiler knows the superclass and current class so not necessary

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampyre(Enemy):
    """Vampyre subclass of Enemy."""
    default_lives=3
    default_hp=12
    
    #def __init__(self, name="Vampyre", lives=default_lives, hit_points=default_hp):
    def __init__(self, name="Vampyre"):
        #super().__init__(name=name, lives=self.default_lives, hit_points=self.default_hp)
        #super().__init__(name=name, lives=lives, hit_points=hit_points)
        super().__init__(name=name, lives=self.default_lives, hit_points=self.default_hp)

    def dodges(self):
        if random.randint(1,3) == 3:
            print("****** {0._name} dodges ******".format(self))
            return True
        else:
            return False
        
    # Method to override take_damage from Enemy class (rewrites it for each instance of Vampyre rather than source for class)
    def take_damage(self, damage, maxhp=12):
        if not self.dodges(): # check if vampire dodges
            super().take_damage(damage=damage, maxhp=maxhp) # call on superclass method take_damage

    
# TODO: Create VampyreKing subclass of Vampyre
# damage inflicted will be divided by 4
# start off with 140 hitpoints

class VampyreKing(Vampyre):
    """VampyreKing subclass of Vampyre."""
    default_lives = 3
    default_hp = 140
    damage_damper=4 # divide incoming damage by this amount for valid classes attacking it

    def __init__(self, name="VampyreKing"):        
        #super().__init__(name=name, lives=self.default_lives, hit_points=default_hp) # parent class no longer has these attributes
        super().__init__(name=name)
        self._lives = self.default_lives
        self._hp = self.default_hp

    # Override Vampyre take_damage method to divide damage by 4
    # Do this indirectly by logging the change in hp
    def take_damage(self, damage, maxhp=default_hp):
        super().take_damage(damage=damage // self.damage_damper) # call on superclass method take_damage() from vampyre class (which includes dodging) rather than top superclass (Enemy)