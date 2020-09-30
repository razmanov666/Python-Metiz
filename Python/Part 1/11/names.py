from name_function import *

print ("Enter 'q' at any time to quit.")
while True:
    first = input("\nPLS give me your first name:\n")
    if first == 'q':
        break
    last = input("PLS give me your last name:\n")
    if last == 'q':
        break
    formatted_name = get_fomatted_name(first, last)
    print("\nNeatly formatted name: " + formatted_name +'.')