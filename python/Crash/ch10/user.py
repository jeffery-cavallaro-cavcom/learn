import json

data = {
    'name': {
        'first': 'Jeffery',
        'last': 'Cavallaro'
    },
    'age': 58
}

filename = 'data/user.json'

try:
    with open(filename) as f:
        values = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        values = data
        json.dump(values, f)

print(values)
