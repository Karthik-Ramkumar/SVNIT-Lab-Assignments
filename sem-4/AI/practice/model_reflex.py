# Model-Based Reflex Agent for 3 tiles cleaning

import random

rooms = ['A', 'B', 'C']
state = {
    'A': random.choice(['Dirty', 'Clean']),
    'B': random.choice(['Dirty', 'Clean']),
    'C': random.choice(['Dirty', 'Clean'])
}

location = 'A'
model = {
    'A': 'Unknown',
    'B': 'Unknown',
    'C': 'Unknown'
}

def next_room(location):
    i = rooms.index(location)
    if i < 2:
        return rooms[i + 1]
    return None

print("Initial State:", state)

while True:
    percept = state[location]
    model[location] = percept   # update internal model

    if percept == 'Dirty':
        print("Location:", location, "-> Clean")
        state[location] = 'Clean'
        model[location] = 'Clean'
    else:
        nxt = next_room(location)
        if nxt:
            print("Location:", location, "-> Move Right")
            location = nxt
        else:
            break

    if model['A'] == 'Clean' and model['B'] == 'Clean' and model['C'] == 'Clean':
        break

print("Final State:", state)