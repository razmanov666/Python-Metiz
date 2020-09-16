famous_human_0 = {"first_name" : 'Lionel', "last_name" : 'Messi', "age" : 33, 
                "city" : 'Barcelona'}
famous_human_1 = {"first_name" : 'Cristiano', "last_name" : 'Ronaldo', "age" : 35, 
                "city" : 'Juventus'}
famous_human_2 = {"first_name" : 'Robert', "last_name" : 'Lewandovski', "age" : 29, 
                "city" : 'Bayern'}
people = [famous_human_0, famous_human_1, famous_human_2]
for human in people:
    full_name = human['first_name'] + ' ' + human['last_name']
    city = human['city']
    age = human['age']
    print('The ' + full_name.title() + ' living in ' + city.title() + 
        ' and his ' + str(age) + ' years old!')
# n = 0
# for key, value in famous_human.items():
#     n+=1
#     print ("\nKey №"+str(n)+": " + key)
#     print ("Value №"+str(n)+": " + str(value))

# print (famous_human["first_name"])
# print (famous_human["last_name"])
# print (famous_human["age"])
# print (famous_human["city"])