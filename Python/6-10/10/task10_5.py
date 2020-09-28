file_path = ('/home/kurama/Документы/Training/'+
            'Python/6-10/10/common_files/like_prog.txt')
with open(file_path, 'a') as file_object:
    while(True):
        text = input("Why do you like a prog? For exit input 'exit'.\n")
        if text == 'exit':
            break
        file_object.write(text + '.\n')
