file_path = ("/home/kurama/Документы/Training/" +
            "Python/6-10/10/common_files/pi_digits_million.txt")
pi_string = ''
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.strip()

birthday = input('Input your birthday, in the form mmddyy: \n')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
# print(pi_string)
# print(len(pi_string))
