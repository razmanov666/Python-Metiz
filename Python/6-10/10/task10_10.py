file_name = ("/home/kurama/Документы/Training/Python" +
            "/6-10/10/common_files/alice.txt")
with open(file_name) as f_object:
    count = f_object.read().lower().split().count('the')
    print(count)