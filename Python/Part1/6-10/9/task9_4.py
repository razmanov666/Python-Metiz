from task9_1_class import *

restaurant = Restaurant('barsa del toro', 'spanish')
print (restaurant.number_served)
restaurant.number_served = 20
print (restaurant.number_served)
restaurant.set_number_served(10)
print (restaurant.number_served)
restaurant.incriment_number_served(90)
print (restaurant.number_served)