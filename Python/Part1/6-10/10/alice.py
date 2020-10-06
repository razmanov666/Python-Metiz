file_path = ('/home/kurama/Документы/Training/Python/6-10/10/'+
            'common_files/alice2.txt')
file_name = 'alice.txt'
try:
    with open(file_path) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the file " + file_name + " does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print ("The file " + file_name + " has about " + str(num_words) + " words.")