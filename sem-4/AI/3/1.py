# do i need to make movement random from B???
#it is rational cause it cleans and moves to the clean rooms.
# cleaning room gives points,moving will remove points.

import random

rooms = ['A', 'B', 'C']
status_index = {'clean': 0, 'dirty': 1}
location = 'A'
# row: (A=0, B=1, C=2)
# col: (clean=0, dirty=1)
rule_matrix = [
    ['MoveRight', 'Suck'],   # from A
    ['MoveRight', 'Suck'],   # from B
    ['MoveLeft',  'Suck']    # from C
]

def move(loc, action):
    i = rooms.index(loc)
    if action == 'MoveRight' and i < 2: # cant go right from C
        return rooms[i + 1]
    if action == 'MoveLeft' and i > 0: # cant go left from A
        return rooms[i - 1]
    return loc

print("percept\t\taction\t\tlocation")
print("------------------------------------------------")

for step in range(10):
    # initializing environment
    env = {
    'A': random.choice(['dirty', 'clean']),
    'B': random.choice(['dirty', 'clean']),
    'C': random.choice(['dirty', 'clean'])
}
    status = env[location]          # agent perceives dirt only when present
    percept = (location, status)

    r = rooms.index(location)
    c = status_index[status]
    action = rule_matrix[r][c]

    print(percept, "\t", action, "\t", location)

    if action == 'Suck':
        env[location] = 'clean' #updating the env after cleaning
    else:
        location = move(location, action)
