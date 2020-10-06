mg_dict = {'country': 'blr', 'population': 20000, 'fact': 'mini city'}
novo_dict = {'country': 'blr', 'population': 20000, 'fact': 'mini city'}
msk_dict = {'country': 'rus', 'population': 10000000, 'fact': 'big city'}
cities = { 'марьина горка': mg_dict, 'новогрудок': novo_dict, 'москва': msk_dict}
for key, city in cities.items():
    print ('Информация о ' + str(key).title() + ': ')
    for k, v in city.items():
        print ('\t' + k + ' is ' + str(v) + '!')