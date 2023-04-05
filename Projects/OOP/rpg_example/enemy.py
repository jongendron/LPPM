#class Enemy:
class Enemy(object): # inherit object superclass (same as above but more verbose, but only in Python 3)
    """Highest superclass of enemies (aside from object class)."""

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else: # enemy died (lost a life)
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hitpoints: {0.hit_points}".format(self)


class Troll(Enemy):  # 1st parameter is a superclass to inherit
    """Troll class enemy."""

    def __init__(self, name="Enemy Troll"): # current class constructor (this call cancels the superclass's constructor)
        Enemy.__init__(self, name=name, lives=1, hit_points=23) # calls on Enemy superclass's constructor (__init__()) as part of Troll()'s __init__()