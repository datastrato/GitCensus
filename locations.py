#
# Display all of the user locations for a repository
#

import pickle

with open('locations.pickle', 'rb') as file:
    locations = pickle.load(file)

locs = {}
no = 0
for person in locations:
    location = locations[person]
    if location not in locs:
        locs[location] = 1
    else:
        locs[location] = locs[location] + 1
    no = no + 1

for location in locs:
    print(f"{location},{locs[location]}")

print(f'{no} locations')