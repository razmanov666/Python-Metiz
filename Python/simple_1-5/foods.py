my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
"""
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
"""
print "My favorite foods:"
for food in my_foods:
    print (food)
print "\nFriend's favorite foods :"
for food in friend_foods:
    print (food)
