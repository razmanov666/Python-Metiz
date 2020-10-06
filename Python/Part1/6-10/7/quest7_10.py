answer = True
places = []
while answer:
    answer = input('Где хочешь отдохнуть?\n\n')
    if answer.lower() == 'quit':
        break
    places.append(answer)
print ('Популярные места: \n')
for place in places:
    print (place.title())