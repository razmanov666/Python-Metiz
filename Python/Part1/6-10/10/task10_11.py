import json

filename = ("/home/kurama/Документы/Training/Python/6-10/10/"+
            "common_files/dogs.txt")

fav_number = input('Input your favorite number:\n')
with open(filename, 'w') as f_obj:
    json.dump(fav_number, f_obj)
