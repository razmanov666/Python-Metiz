import json

filename = ("/home/kurama/Документы/Training/Python/6-10/10/"+
            "common_files/dogs.txt")

try:
    with open(filename) as f_obj:
        msg = json.load(f_obj)
except FileNotFoundError:
    print('File Not Found')
else:
    print('I know your favorite number, is ' + msg + '!')