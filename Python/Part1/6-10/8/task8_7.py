def make_album(author, album, tracks = ''):
    info_album = {'Author': author.title(), 'Album' : album.title()}
    if '' != tracks >= 0:
        info_album['num of tracks'] = tracks
    return info_album

# print (make_album('LP', 'Hybrid Theory', 8))
# print (make_album('BMTH', 'Sempiternal', 10))
# print (make_album('Леха', 'Домашний реп'))

print ('Input vsyakoe govno:\n')
while True:
    author = input('\nInput author: \n')
    if author == 'q':
        print ('Good buy, uebische')
        break
    album = input('Input album: \n')
    if album == 'q':
        print ('\nGood buy, uebische')
        break
    print (make_album(author, album))
