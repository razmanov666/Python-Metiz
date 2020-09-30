filename1 = ("/home/kurama/Документы/Training/Python/6-10/10/"+
            "common_files/cats.txt")

filename2 = ("/home/kurama/Документы/Training/Python/6-10/10/"+
            "common_files/dog1s.txt")

def read_file(filename):
    """Чтение файла"""
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
read_file(filename1)
read_file(filename2)
