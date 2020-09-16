import favorite_languages

people = ['leha', 'phil', 'jen', 'sashka']
for name in people:
    if name in favorite_languages.favorite_languages_list.keys():
        print('Спасибо, ' + name.title())
    if name not in favorite_languages.favorite_languages_list.keys():
        print('Пройди тест, ' + name.title())
