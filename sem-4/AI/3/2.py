import random
#Emergency lever overrides,Obstacle detection overrides train movement
# percept values
trainStates = ['detected', 'notDetected']
obstacleStates = ['clear', 'obstacle']
emergencyStates = ['neutral', 'active']

# percept (trainDetected, obstaclePresent, emergencyLever)
# action (gateArm, siren, trainSignal)
ruleTable = {
    ('detected', 'obstacle', 'neutral'): ('lower', 'on', 'red'),
    ('detected', 'obstacle', 'active'):  ('lower', 'on', 'red'),
    ('detected', 'clear', 'active'):     ('lower', 'on', 'red'),
    ('detected', 'clear', 'neutral'):    ('lower', 'on', 'green'),
    ('notDetected', 'obstacle', 'neutral'): ('lower', 'on', 'red'), # RAISE?
    ('notDetected', 'obstacle', 'active'):  ('lower', 'on', 'red'), # RAISE?
    ('notDetected', 'clear', 'active'):     ('lower', 'on', 'red'),
    ('notDetected', 'clear', 'neutral'):    ('raise', 'off', 'green')
}

location = 'levelCrossing'

print("percept (train, obstacle, emergency)\taction (gate, siren, signal)\tlocation")
print("--------------------------------------------------------------------------")

for step in range(10):
    trainDetected = random.choice(trainStates)
    obstaclePresent = random.choice(obstacleStates)
    emergencyLever = random.choice(emergencyStates)

    percept = (trainDetected, obstaclePresent, emergencyLever)

    action = ruleTable[percept]

    print(percept, "\t", action, "\t", location)