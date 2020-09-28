import json

filename = ('/home/kurama/Документы/Training/'+
            'Python/6-10/10/common_files/username.json')
with open(filename) as f_obj:
    username = json.load(f_obj)
    print ('Hello, ' + username)