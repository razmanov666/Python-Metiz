barsik = {'name': 'barsik', 'animal': 'cat', 'owner': 'dima'} 
kesha = {'name': 'kesha', 'animal': 'parrot', 'owner': 'dasha'}  
scooby_doo = {'name': 'scooby doo',  'animal': 'dog', 'owner': 'lesha'}
pets = [barsik, kesha, scooby_doo]
for pet in pets:
    i = 0
    for k,v in pet.items():
        i += 1
        if i == 2:
            print (k.title() +' is ' + v + '.')
        else:
            print (k.title() +' is ' + v.title() + '.')
    print()