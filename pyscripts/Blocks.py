import random
import numpy as np
import torch
import pyorca

M_PI = 3.14159265358979323846

goals = pyorca.V_Vec2()

def setupScenario(sim):

    sim.setTimeStep(0.25);

    sim.setAgentDefaults(15.0, 10, 5.0, 5.0, 2.0, 2.0, pyorca.Vector2())
    for i in range(5):
        for j in range(5):
            sim.addAgent(pyorca.Vector2(55.0 + i * 10.0,  55.0 + j * 10.0));
            goals.append(pyorca.Vector2(-75.0, -75.0));

            sim.addAgent(pyorca.Vector2(-55.0 - i * 10.0,  55.0 + j * 10.0));
            goals.append(pyorca.Vector2(75.0, -75.0));

            sim.addAgent(pyorca.Vector2(55.0 + i * 10.0, -55.0 - j * 10.0));
            goals.append(pyorca.Vector2(-75.0, 75.0));

            sim.addAgent(pyorca.Vector2(-55.0 - i * 10.0, -55.0 - j * 10.0));
            goals.append(pyorca.Vector2(75.0, 75.0));
        
    


    obstacle1 = pyorca.V_Vec2()
    obstacle2 = pyorca.V_Vec2()
    obstacle3 = pyorca.V_Vec2()
    obstacle4 = pyorca.V_Vec2()

    obstacle1.append(pyorca.Vector2(-10.0, 40.0));
    obstacle1.append(pyorca.Vector2(-40.0, 40.0));
    obstacle1.append(pyorca.Vector2(-40.0, 10.0));
    obstacle1.append(pyorca.Vector2(-10.0, 10.0));

    obstacle2.append(pyorca.Vector2(10.0, 40.0));
    obstacle2.append(pyorca.Vector2(10.0, 10.0));
    obstacle2.append(pyorca.Vector2(40.0, 10.0));
    obstacle2.append(pyorca.Vector2(40.0, 40.0));

    obstacle3.append(pyorca.Vector2(10.0, -40.0));
    obstacle3.append(pyorca.Vector2(40.0, -40.0));
    obstacle3.append(pyorca.Vector2(40.0, -10.0));
    obstacle3.append(pyorca.Vector2(10.0, -10.0));

    obstacle4.append(pyorca.Vector2(-10.0, -40.0));
    obstacle4.append(pyorca.Vector2(-10.0, -10.0));
    obstacle4.append(pyorca.Vector2(-40.0, -10.0));
    obstacle4.append(pyorca.Vector2(-40.0, -40.0));

    sim.addObstacle(obstacle1);
    sim.addObstacle(obstacle2);
    sim.addObstacle(obstacle3);
    sim.addObstacle(obstacle4);

    sim.processObstacles();


def updateVisualization(sim):
	print(sim.getGlobalTime())

	for i in range(sim.getNumAgents()):
		pos = sim.getAgentPosition(i)
		print(pos.x(), pos.y())


def setPreferredVelocities(sim):
	num_agent = int(sim.getNumAgents())

	for i in range(num_agent):
		goalVector = goals[i] - sim.getAgentPosition(i)

		if (pyorca.absSq(goalVector) > 1.0):
			goalVector = pyorca.normalize(goalVector)


		sim.setAgentPrefVelocity(i, goalVector)

		angle = random.random() * 2.0 * M_PI 
		dist  = random.random() * 0.0001 

		sim.setAgentPrefVelocity(i, sim.getAgentPrefVelocity(i) +
		                          dist * pyorca.Vector2(np.cos(angle), np.sin(angle)))



def reachedGoal(sim):
	num_agent = sim.getNumAgents()
	for i in range(num_agent):
		if (pyorca.absSq(sim.getAgentPosition(i) - goals[i]) > 20.0 * 20.0): 
			return False
	
	return True


sim = pyorca.RVOSim()
setupScenario(sim)

while True:
	updateVisualization(sim)
	setPreferredVelocities(sim)
	sim.doStep()

	if (reachedGoal(sim)):
		break


