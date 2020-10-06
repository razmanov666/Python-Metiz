glosary = {
    '1':['один', 'one'],
    '2':['два', 'two'],
    '3':['три', 'three'],
    '4':['четыре', 'four'],
    '5':['пять', 'five'],
    '0':['nil', 'ноль'],
    '9':['девять', 'nine'],
    '8':['восемь', 'eight'],
    '7':['семь', 'seven'],
    '6':['шесть', 'six'],
    }
for k, value in sorted(glosary.items()):
    i = 0
    for v in value:
        i += 1
        if i == 1:
            print((k + ' - это ' + v), end=' ')
        else:
            print ('и ' + v)
