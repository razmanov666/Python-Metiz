favorite_languages_list = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages_list.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " + 
            favorite_languages_list[name][0].title())
    elif len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are: ")
        for language in languages:
            print("\t- " + language.title())