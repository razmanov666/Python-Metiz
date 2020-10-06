file_path = ("/home/kurama/Документы/Training/" +
            "Python/6-10/10/common_files/guest.txt")
username = input('Input your name:\n')
with open(file_path, "a") as file_object:
    file_object.write(username + '\n')