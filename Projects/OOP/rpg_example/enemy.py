#class Enemy:
class Enemy(object): # inherit object superclass (same as above but more verbose, but only in Python 3)
    """Highest superclass of enemies (aside from object class)."""

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage, maxhp=30): # TODO: is there a way to replace 30 with the maxhp for a subclass?
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else: # enemy died (lost a life)
            self.lives -= 1
            self.hit_points = maxhp
            print(f"I lost 1 life and my hp has been reset to {maxhp}")

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hitpoints: {0.hit_points}".format(self)


class Troll(Enemy):  # 1st parameter is a superclass to inherit
    """Troll subclass of Enemy."""

    def __init__(self, name="Enemy Troll"): # current class constructor (this call cancels the superclass's constructor)
        #Enemy.__init__(self, name=name, lives=1, hit_points=23) # Python 2: calls on Enemy superclass's constructor (__init__()) as part of Troll()'s __init__()
        #super(Troll, self).__init__(name=name, lives=1, hit_points=23) # Python 3 way
        super().__init__(name=name, lives=1, hit_points=23) # Compiler knows the superclass and current class so not necessary

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))


#TODO: Create Vampyre class as subclass of Enemy
# They should have 3 lives, and take 12 hitpoints of damge
# Test with two or three instances.
# Test if trolls can take damage too.
class Vampyre(Enemy):
    """Vampyre subclass of Enemy."""
    default_lives=3
    default_hp=12
    
    def __init__(self, name="Vampyre"):
        super().__init__(name=name, lives=self.default_lives, hit_points=self.default_hp)

    
