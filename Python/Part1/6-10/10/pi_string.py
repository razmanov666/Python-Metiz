file_path = ("/home/kurama/Документы/Training/" +
            "Python/6-10/10/common_files/pi_digits_million.txt")
pi_string = ''
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))
