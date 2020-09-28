print("Введите 2 числа, чтобы я их посчитал.")
print("Введите 'q', чтобы выйти из программы.")

while True:
    first_number = input("Введите первое число:\n")
    if first_number == 'q':
        break
    second_number = input("Введите первое число: \n")
    if second_number == 'q':
        break
    try:
        input_first = int(first_number)
        input_second = int(second_number)
    except ValueError:
        print('Некорректно введенные данные!')
    else:
        print ("Сумма = " + str(input_first + input_second))