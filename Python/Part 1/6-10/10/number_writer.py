import json

numbers = [2,3,4,5,7,0]
filename = 'Python/6-10/10/common_files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)