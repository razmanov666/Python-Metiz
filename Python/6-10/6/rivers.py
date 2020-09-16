big_rivers = {
    'nile': 'egypt',
    'volga': 'russia',
    'amazon': 'brazil',
    }
for k, v in big_rivers.items():
    print("The " + k.title() +" runs through " + v.title() + '.')
print("\nA big rivers is: ")
for k in big_rivers.keys():
    print(k.title())
print("\nCountries which have a big rivers: ")
for v in big_rivers.values():
    print(v.title())