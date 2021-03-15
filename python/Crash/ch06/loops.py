person = {
    'name': {
        'first': 'Jeffery',
        'last': 'Cavallaro'
    },
    'sex': 'male',
    'address': {
        'street': '38712 Almaden Place',
        'city': 'Fremont',
        'state': 'CA',
        'zip': '94536'
    },
    'phone': {
        'home': '510-797-7712',
        'mobile': '510-697-7231'
    },
    'birthday': {
        'month': 7,
        'day': 19,
        'year': 1962
    },
    'deceased': False
}

for k, v in person.items():
    if type(v) is dict:
        print(f"{k}:")
        for k2 in v.keys():
            print(f"    {k2}: {v[k2]}")
    else:
        print(f"{k}: {v}")
