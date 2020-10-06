from task9_1_class import *

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = ['orange', 'onigiri', 'soletto']

    def get_flavors(self):
        print ("We have: ")
        for flavor in self.flavors:
            print("- " + flavor)