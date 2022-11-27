from game.casting.actor import Actor

class Object(Actor):

    def __init__(self):
        super().__init__()

#Determined if the player were to get or lose points if it hit a gem or a stone.
    def calculate_points(self):
        points = 0

        if (self.get_text() == '*'):
            points = 1
        else:
            points = -1
        
        return points