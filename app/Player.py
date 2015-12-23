from GameObject import GameObject
from Action import Action

class Player(GameObject):
    def __init__(self,name,id):
        super(GameObject, self).__init__()
        self.name = name
        self.direction = 0
        self.amunition = 10
        self.action = Action.NONE
        self.id = id

    def reload(self):
        self.amunition = 10;

    #on update we switch depending on what action we have been given
    def update(self):
        if self.alive == True:
            if self.action is Action.MOVE:
                self.move(1,direction)
            elif self.action is Action.FIRE:
                 self.amunition -=1
            elif self.action is Action.TURNNORTH:
                self.direction = 0
            elif self.action is Action.TURNEAST:
                self.direction = 90
            elif self.action is Action.TURNSOUTH:
                self.direction = 180
            elif self.action is Action.TURNWEST:
                self.direction = 270


        #reset the action
        self.action == Action.NONE
