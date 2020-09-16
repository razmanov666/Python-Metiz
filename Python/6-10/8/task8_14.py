def make_car(brend, type_car, **getted_info):
    info_car = {}
    info_car['brend'] = brend
    info_car['type_car'] = type_car
    for k, v in getted_info.items():
        info_car[k] = v
    return info_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)