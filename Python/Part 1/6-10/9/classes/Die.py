from random import randint

class Die():
    """Кубики"""
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        """Бросок кубика"""
        print(str(randint(1, self.sides)))