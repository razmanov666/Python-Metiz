import sys
sys.path.insert(0,'/home/kurama/Документы/Training/Python/6-10/9/classes')
from Die import *

sides_6 = Die()
sides_10 = Die(10)
sides_20 = Die(20)
#sides_6.roll_die()

def roll(die):
    for num in range(10):
        die.roll_die()

# roll(sides_6)
# roll(sides_10)
roll(sides_20)