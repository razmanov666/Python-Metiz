import json

filename = 'Python/6-10/10/common_files/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)