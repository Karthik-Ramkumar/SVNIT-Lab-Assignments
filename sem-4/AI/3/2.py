import random
#Emergency lever overrides,Obstacle detection overrides train movement so it is rational
# percept values
trainStates = ['detected', 'notDetected']
obstacleStates = ['clear', 'obstacle']
emergencyStates = ['neutral', 'active']

# percept (trainDetected, obstaclePresent, emergencyLever)
# action (gateArm, siren, trainSignal)

# RULE TABLE [train, obstacle, emergency, actionIndex]

ruleTable = [
 ['detected','obstacle','neutral',0],
 ['detected','obstacle','active',0],
 ['detected','clear','active',1],
 ['detected','clear','neutral',2],
 ['notDetected','obstacle','neutral',0],    # should we not raise the gate here?
 ['notDetected','obstacle','active',0],         
 ['notDetected','clear','active',1],
 ['notDetected','clear','neutral',3]
]

#  ACTION TABLE [gate, siren, signal, cost]

actionTable = [
 ['lower','on','red',5],     # action 0
 ['lower','on','red',4],     # action 1
 ['lower','on','green',3],   # action 2
 ['raise','off','green',1]   # action 3
]

location = 'levelCrossing'

print("percept (train, obstacle, emergency)\taction (gate, siren, signal, cost)\tlocation")
print("-------------------------------------------------------------------------------------")

for step in range(10):
    trainDetected = random.choice(trainStates)
    obstaclePresent = random.choice(obstacleStates)
    emergencyLever = random.choice(emergencyStates)

    percept = (trainDetected, obstaclePresent, emergencyLever)

    actionIndex = None
    for row in ruleTable:
        if row[0]==trainDetected and row[1]==obstaclePresent and row[2]==emergencyLever:
            actionIndex = row[3]
            break

    action = actionTable[actionIndex]

    print(percept,"\t",action,"\t",location)
