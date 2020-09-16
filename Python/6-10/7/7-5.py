active = True
i = 0
while active:
    i += 1
    if i == 5:
        active = False
    msg = input('Введите возраст: ')
    if msg == 'quit':
        break
    if int(msg) < 3:
        print ('price: Free')
    elif 3 <= int(msg) <= 12:
        print ('price: 10$')
    elif int(msg) > 12:
        print ('price: 15$')