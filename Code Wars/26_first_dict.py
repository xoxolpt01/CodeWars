
slov = {'green': 'yellow',
        'yellow': 'red',
        'red': 'green'
        }

def update_light(current):
    return slov[current]

print(update_light('yellow'))