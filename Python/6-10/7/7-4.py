prompt = "\nВведите дополнение для пиццы:"
prompt += "\nНапишите quit чтобы выйти. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)