file_path = ('/home/kurama/Документы/Training/'+
            'Python/6-10/10/common_files/learning python.txt')
string = ''
with open(file_path) as file_object:
    lines = file_object.readlines()
    contents = file_object.read()
    print(contents)
    for line in lines:
        string += line
    print(string)
    
print(string)