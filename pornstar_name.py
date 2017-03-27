

import random


names = []

first_names = [
    'Taylor',
    'Anna',
    'Carla',
    'Frankie',
    'Roxanne',
    'Tess',
    'Cat',
    'Michel',
    'Mel',
    'Allison',
    'Sadie',
    'Sam',
    'Alex',
    'Lexi'
]
last_names = [
    'Love',
    'Lou',
    'Oslo',
    'York',
    'Boss',
    'Kong',
    'Ruby',
    'Martin',
    'Bea',
    'James',
    'Rose',
    'Cane'
]

while True:
    firstname = random.choice(first_names)
    lastname = random.choice(last_names)
    pornstar_name = '{0} {1}'.format(firstname, lastname)
    if pornstar_name in names:
        continue
    else:
        names.append(pornstar_name)

    print(pornstar_name)
    desition = input("Continue? Y/n")
    if desition == 'n':
        print('Your pornstar name is: {0}'.format(pornstar_name))
        break
