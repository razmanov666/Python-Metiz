def count_words(file_name):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(file_name) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        # print("Sorry, the file " + file_name + " does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " 
            + str(num_words) +" words.")

file_name = ("/home/kurama/Документы/Training/Python/6-10/10/" +
            "common_files/alice.txt")
filenames = [file_name, 'siddhartha.txt', 'division.txt', 'word_count.py']          
for filename in filenames:
    count_words(filename)