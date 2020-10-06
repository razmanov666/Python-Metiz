print("Give me two numbers, and I will divide them.")
print("Enter 'q' tu quit.")


while True:
    first_number = input("Input first number:\n")
    if first_number == 'q':
        break
    second_number = input("Input second number:\n")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)