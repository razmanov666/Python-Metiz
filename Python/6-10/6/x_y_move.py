alien_0 = {"color": "green", "points": 5}
# print (alien_0)
alien_0["x"] = 0
alien_0["y"] = 0
stop = False
i = 0
while (stop == False):
    i += 1
    print ("\n\tInput vector.\n\tVariants: 'left', 'right', 'up', 'down'.")
    my_input = input("\tFor stopped game print 'exit'\n\n\t")
    if my_input == "left":
        alien_0["x"] -= 1
    elif my_input == "up":
        alien_0["y"] += 1
    elif my_input == "down":
        alien_0["y"] -= 1
    elif my_input == "right":
        alien_0["x"] += 1
    elif my_input == "exit":
        stop = True
    else:
        print ("\tIncorrect input!")
    print ("\tYou now in x = "+str(alien_0["x"])+" and y = "+str(alien_0["y"]))
print ("You do " + str(i)+" steps")