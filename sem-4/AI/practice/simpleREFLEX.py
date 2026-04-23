import random
rooms = ['A', 'B', 'C']
rules = [    
    ['clean',     'right', 'right'],  # A
    ['left', 'clean',      'right'],  # B
    ['left', 'left',  'clean']        # C
]

location = 'A'

def move(location,action):
    i = rooms.index(location)
    if action == "right" and i < 2:
        return rooms[i+1]
    if action == "left" and i > 0:
        return rooms[i-1]
    return location

print("percept action location")

for state in range(5):
    dirty_room = random.choice(['A', 'B', 'C'])
    percept = (location, dirty_room)

    r = rooms.index(location)
    c = rooms.index(dirty_room)
    action = rules[r][c]
    print(percept,action,location)
    if action != 'clean':
        location = move(location,action)
             