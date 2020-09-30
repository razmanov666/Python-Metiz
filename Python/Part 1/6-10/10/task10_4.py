file_path = ("/home/kurama/Документы/Training/" +
            "Python/6-10/10/common_files/guest_book.txt")
with open(file_path, 'a') as file_object:
    while(True):
        username = input("Input your name. For exit input 'exit'.\n")
        if username == 'exit':
            break
        file_object.write("Hello, " + username + '.\n')
