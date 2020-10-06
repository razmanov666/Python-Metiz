import task8_9

great_fokusniki = []
def make_great(arr, arr2):
    i = 0
    for el in arr:
        arr2.append('Great'+el)
        i += 1
    print()
    return arr2

great_fokusniki = make_great(task8_9.fokusniki, great_fokusniki)
task8_9.show_magicans(task8_9.fokusniki)
print()
task8_9.show_magicans(great_fokusniki)