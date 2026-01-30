# we recieve percept as (current_location, dirty_room)
import random
rooms = ['A', 'B', 'C']

# columns: dirt at A=0, B=1, C=2
# rows: current location A=0, B=1, C=2
rule_matrix = [
    ['clean',     'MoveRight', 'MoveRight'],  # A
    ['MoveLeft', 'clean',      'MoveRight'],  # B
    ['MoveLeft', 'MoveLeft',  'clean']        # C
]

location = 'A' 

def move(loc, action):
    i = rooms.index(loc)
    if action == 'MoveRight' and i < 2:
        return rooms[i + 1]
    if action == 'MoveLeft' and i > 0:
        return rooms[i - 1]
    return loc

print("percept\t\t\taction\t\tlocation")
print("------------------------------------------------")

for step in range(10):
    dirty_room = random.choice(['A', 'B', 'C'])
    percept = (location, dirty_room)

    r = rooms.index(location)
    c = rooms.index(dirty_room)
    action = rule_matrix[r][c]

    print(percept, "\t", action, "\t", location)

    if action != 'clean':
        location = move(location, action)
