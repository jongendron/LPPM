class Player(object):

    def __init__(self, name):
        self._name = name
        #self.lives = 3 # fails because the property `lives` has higher priority than attribute and causes infinite recursion
        self._lives = 3 # intended as local
        self._level = 1 # must be >= 1
        self._score = 5000
        #self._score = self._level * 1000 - 1000

    # Getter method to retrieve # lives
    def _get_lives(self):
        return self._lives
    
    # Setter method to define # lives
    def _set_lives(self, lives):
        if lives >= 0: # limit to 0 or above
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0
    
    def _get_level(self):
        return self._level
    
    def _set_level(self, level):
        if level > 0: # limit level 1 or above
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")
            err = 1 - level # 1 - -2 = 3
            delta = level - self._level + err # -2 - 3 = -5 + 3 = -2 
            self._score += delta * 1000
            self._level = 1
            
    # property(self, fget=`process to get data`, fset=`process to store data`)
    # more info: https://realpython.com/python-property/#:~:text=Python's%20property()%20is%20the,use%20it%20without%20importing%20anything.
    # don't name a property same name as attribute
    #lives = property(_get_lives(), _set_lives()) # incorrect, sets fset=return value than actual function (same with fset)
    lives = property(_get_lives, _set_lives) # method/property that accesses _get_lives & _set_lives
    level = property(_get_level, _set_level)
    # What is returned when you print class instance
    def __str__(self):
        #return "Name: {0}, Lives: {1}, Level: {2}, Score: {3}" \
        #    .format(self._name, self.lives, self.level, self.score)
        return "Name: {0._name}, Lives: {0.lives}, Level: {0.level}, Score {0._score}".format(self)
        
    # TODO: Modify Player class so the players' scores increase by 1000
    # TODO: every time their level increases by one.
    # TODO: i.e. two level ups -> +2000 pts to score
    # TODO: if they go down a level they also lose 1000 pts
    # TODO: players can't go below level 1
    # TODO: Do this using properties
